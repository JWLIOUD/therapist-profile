# 最新待辦事項

更新日期：2026-06-19

## 最高優先

- [ ] 在 Google Search Console 驗證 `yuchienpsy.com`。
- [ ] 在 Google Search Console 提交 `https://yuchienpsy.com/sitemap.xml`。
- [ ] 發布後用 URL Inspection 檢查 `https://yuchienpsy.com/talks.html`，並在 live test 通過後要求建立索引。
- [ ] 發布後檢查 `https://yuchienpsy.com/favicon.ico` 是否回 `200`。
- [ ] 發布後用 URL Inspection 檢查首頁 site name 訊號；若已 indexed/requested/on Google，不重複要求建立索引。
- [ ] 用 URL Inspection 檢查一篇文章，例如 `https://yuchienpsy.com/articles/addiction-01.html`。
- [ ] 若文章尚未索引，對重要文章按「要求建立索引」。
- [ ] 提供下一篇要新增的文章正文、分類與希望的 URL slug。
- [ ] 提供需要修改的服務資訊新版文字。

## 固定流程

- [x] 建立「新增文章」工作流。
- [x] 建立「修改服務資訊」工作流。
- [x] 建立「發布前檢查」工作流。
- [ ] 之後每次新增文章都同步更新文章列表、系列頁、sitemap、meta 與 canonical。
- [ ] 之後每次修改服務資訊都同步檢查首頁、CTA、LINE 連結與手機版。
- [ ] 每次發布前執行發布前檢查。

## SEO 改善

- [x] 檢查 sitemap 是否包含所有應收錄頁面。
- [x] 檢查正式站每個 sitemap URL 是否回 `200`。
- [ ] 為重要文章補更明確的 meta description。
- [x] 加強首頁到文章專區與重要文章的內部連結。
- [ ] 考慮加入 `WebSite`、`Person`、`Article` 結構化資料一致性檢查。

## 文件維護

- [ ] 補完整 `README.md`。
- [ ] 整理 `tools/generate_articles.py` 的外部 Word 來源與使用條件。
- [ ] 評估加入 GitHub Actions 做連結與 sitemap 檢查。
