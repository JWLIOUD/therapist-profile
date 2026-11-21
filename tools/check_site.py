#!/usr/bin/env python3
"""Deterministic static checks for the yuchienpsy.com HTML site (stdlib only)."""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE_HOSTS = {"yuchienpsy.com", "www.yuchienpsy.com"}

# Explicit exceptions: redirects are expected to resolve outside this static tree.
# Add normalized source paths here only when a real redirect is documented.
REDIRECT_PATHS: set[str] = set()
# These files are deliberately non-indexable. They are checked for isolation below.
NOINDEX_PATHS = {
    "drafts/workplace-mental-health-seo-test.html",
    "drafts/seo-options/index.html",
    "drafts/seo-options/option-a-workplace-article.html",
    "drafts/seo-options/option-b-workplace-hub.html",
    "drafts/seo-options/option-c-workplace-series.html",
}
PUBLIC_NAV_TAGS = {"nav", "header", "footer"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: Counter[str] = Counter()
        self.links: list[tuple[str, str]] = []
        self.canonicals: list[str] = []
        self.titles: list[str] = []
        self.h1_count = 0
        self.robots: list[str] = []
        self._title = False
        self._title_text = ""
        self._h1_depth = 0
        self._nav_depth = 0
        self.nav_links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if a.get("id"):
            self.ids[a["id"]] += 1
        if tag == "h1":
            self.h1_count += 1
            self._h1_depth += 1
        if tag == "title":
            self._title = True
            self._title_text = ""
        if tag in PUBLIC_NAV_TAGS:
            self._nav_depth += 1
        if tag in ("a", "link", "script", "img", "source", "iframe", "audio", "video"):
            attr = "href" if tag in ("a", "link") else "src"
            value = a.get(attr)
            if value:
                self.links.append((attr, value.strip()))
                if tag == "a" and self._nav_depth:
                    self.nav_links.append((attr, value.strip()))
        if tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            if a.get("href"):
                self.canonicals.append(a["href"].strip())
        if tag == "meta" and (a.get("name") or "").lower() == "robots":
            self.robots.append((a.get("content") or "").lower())

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._h1_depth:
            self._h1_depth -= 1
        if tag == "title" and self._title:
            self._title = False
            self.titles.append(self._title_text.strip())
        if tag in PUBLIC_NAV_TAGS and self._nav_depth:
            self._nav_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._title:
            self._title_text += data


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def html_pages() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.html")
        if ".git" not in p.parts and "docs" not in p.relative_to(ROOT).parts
    )


def public_pages() -> list[Path]:
    # Drafts are parsed separately for noindex isolation, never treated as public content.
    return [p for p in html_pages() if "drafts" not in p.relative_to(ROOT).parts]


def is_noindex(parser: PageParser) -> bool:
    return any("noindex" in meta for meta in parser.robots)


def local_target(source: Path, raw: str) -> tuple[Path | None, str | None]:
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc:
        if parsed.hostname and parsed.hostname.lower() in SITE_HOSTS:
            path = unquote(parsed.path).lstrip("/") or "index.html"
        else:
            return None, None
    else:
        path = unquote(parsed.path)
        if path.startswith("/"):
            path = path.lstrip("/")
        else:
            path = (source.parent / path).as_posix()
        if not path:
            path = relpath(source)
    target = (ROOT / path).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None, None
    return target, unquote(parsed.fragment) if parsed.fragment else None


def sitemap_paths() -> tuple[list[str], list[str]]:
    file = ROOT / "sitemap.xml"
    if not file.exists():
        return [], ["sitemap.xml is missing"]
    try:
        urls = [el.text.strip() for el in ET.parse(file).iter() if el.tag.endswith("}loc") and el.text]
        return urls, []
    except ET.ParseError as exc:
        return [], [f"sitemap.xml: invalid XML: {exc}"]


def main() -> int:
    global ROOT
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT, help="site root (defaults to this checkout)")
    args = ap.parse_args()
    ROOT = args.root.resolve()

    errors: list[str] = []
    pages = public_pages()
    parsed_pages: dict[Path, PageParser] = {}
    for rel in sorted(NOINDEX_PATHS):
        page = ROOT / rel
        if page.is_file():
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8"))
            parsed_pages[page] = parser
    canonical_owner: dict[str, str] = {}
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parsed_pages[page] = parser
        rel = relpath(page)
        indexed = not is_noindex(parser)
        if indexed:
            if parser.h1_count != 1:
                errors.append(f"{rel}: indexable page has {parser.h1_count} H1 elements (expected 1)")
            if len(parser.titles) != 1 or not parser.titles[0]:
                errors.append(f"{rel}: indexable page has {len(parser.titles)} non-empty title elements (expected 1)")
            if len(parser.canonicals) != 1:
                errors.append(f"{rel}: indexable page has {len(parser.canonicals)} canonical links (expected 1)")
            for canonical in parser.canonicals:
                key = canonical.rstrip("/")
                if key in canonical_owner:
                    errors.append(f"canonical duplicate: {rel} and {canonical_owner[key]} both use {canonical}")
                else:
                    canonical_owner[key] = rel

        for attr, value in parser.links:
            target, fragment = local_target(page, value)
            if target is None:
                continue
            target_rel = target.relative_to(ROOT).as_posix()
            if not target.exists():
                if target_rel not in REDIRECT_PATHS:
                    errors.append(f"{rel}: local {attr} target missing: {value}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed_pages.get(target)
                if target_parser is None:
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed_pages[target] = target_parser
                if not target_parser.ids.get(fragment):
                    errors.append(f"{rel}: fragment #{fragment} missing in {target_rel}")

        for ident, count in parser.ids.items():
            if count > 1:
                errors.append(f"{rel}: duplicate id={ident!r} ({count} occurrences)")

    sitemap, sitemap_errors = sitemap_paths()
    errors.extend(sitemap_errors)
    seen_sitemap: set[str] = set()
    for url in sitemap:
        parsed = urlparse(url)
        if parsed.hostname and parsed.hostname.lower() not in SITE_HOSTS:
            errors.append(f"sitemap URL uses unexpected host: {url}")
            continue
        path = unquote(parsed.path).lstrip("/") or "index.html"
        if path in seen_sitemap:
            errors.append(f"sitemap duplicate URL: {url}")
        seen_sitemap.add(path)
        target = ROOT / path
        if not target.is_file():
            errors.append(f"sitemap URL has no local file: {url} -> {path}")
        elif target.suffix.lower() == ".html":
            parser = parsed_pages.get(target)
            if parser and is_noindex(parser):
                errors.append(f"noindex page listed in sitemap: {path}")
        if path in NOINDEX_PATHS or path.startswith("docs/"):
            errors.append(f"non-public page listed in sitemap: {path}")

    for rel in sorted(NOINDEX_PATHS):
        page = ROOT / rel
        parser = parsed_pages.get(page)
        if page.exists() and parser and not is_noindex(parser):
            errors.append(f"draft boundary: {rel} is expected to carry noindex")
    for page, parser in parsed_pages.items():
        rel = relpath(page)
        if is_noindex(parser):
            continue
        for _, value in parser.nav_links:
            target, _ = local_target(page, value)
            if target and target.is_relative_to(ROOT) and relpath(target) in NOINDEX_PATHS:
                errors.append(f"noindex page exposed in public navigation: {rel} -> {value}")

    print(f"Checked {len(pages)} HTML files; sitemap contains {len(sitemap)} URLs.")
    print(f"Documented redirect exceptions: {', '.join(sorted(REDIRECT_PATHS)) or '(none)'}")
    print(f"Expected noindex exceptions: {', '.join(sorted(NOINDEX_PATHS))}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f" - {error}")
        return 1
    print("PASS: no static issues found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
