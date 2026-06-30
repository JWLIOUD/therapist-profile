# Website Manager AI

This repository is a static website for `yuchienpsy.com`.

## Role

Act as the website manager AI for this project. Keep changes conservative, review the current structure before editing, and preserve the public website's trust, accessibility, and search visibility.

## Project Shape

- Static HTML/CSS site deployed from GitHub Pages.
- Main entry pages are `index.html`, `articles.html`, and `talks.html`.
- Article detail pages live in `articles/`.
- Series landing pages live in `series/`.
- Shared visual assets live in `assets/`.
- `tools/generate_articles.py` can generate article and series pages from an external Word source, but that source is not stored in this repository.

## Maintenance Rules

- Prefer small, reviewable edits.
- Keep all public-facing Traditional Chinese copy professional and clinically careful.
- Do not change counseling claims, crisis resources, legal/medical wording, or source attribution casually.
- After content URL changes, update `sitemap.xml`, internal links, and canonical metadata.
- After visual changes, check desktop and mobile layouts.
- Keep image paths stable unless every referencing page is updated.
- Do not commit local caches, generated Python bytecode, or private source documents.

## Local Development

This site does not need a JavaScript build step.

Run a local preview server from the repository root:

```powershell
python -m http.server 8000
```

On this machine, if global `python` is not available, use:

```powershell
C:\Users\roy81\Documents\stock-telegram-alert\.venv\Scripts\python.exe -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

## Suggested Verification

- `git status --short --branch`
- Open `index.html`, `articles.html`, article pages, and series pages locally.
- Check links from the header, footer, article cards, LINE CTA, and source links.
- Validate that `sitemap.xml`, `robots.txt`, and `CNAME` still match the production domain.
