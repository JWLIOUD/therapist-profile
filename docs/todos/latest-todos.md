# 最新待辦事項

更新日期：2026-07-04

## 最高優先

- [ ] 使用者從 Google 搜尋結果 logo 候選中選擇 A / B / C；選定後再替換正式 favicon 套件。
- [x] 發布後檢查 `https://yuchienpsy.com/favicon.ico`、`https://yuchienpsy.com/assets/favicon-48.png`、`https://yuchienpsy.com/assets/favicon-192.png`、`https://yuchienpsy.com/assets/site-icon-512.png` 是否都回 `200`。
- [ ] 發布後用 Google Search Console URL Inspection 檢查 `https://yuchienpsy.com/`，確認 Google 看到新版首頁與 favicon 設定。
- [ ] 若 Search Console 已顯示首頁「已要求建立索引」、已在 Google 服務中、或已編入索引，不得再次按 Request indexing；只記錄狀態與時間，避免浪費每日額度。
- [ ] 用實際瀏覽器 Google 搜尋 `黃郁倩心理師`、`黃郁倩諮商心理師`、`黃郁倩心理師 yuchienpsy.com`、`site:yuchienpsy.com 黃郁倩心理師`，截圖並記錄搜尋結果網站名稱、favicon、排名與摘要。
- [ ] 若實際搜尋截圖驗收未通過，依失敗原因持續修正；若需要 Search Console 權限、瀏覽器登入或使用者判斷，先停下與使用者討論。
- [ ] 發布後 3-14 天觀察 Google 搜尋結果是否開始顯示「黃郁倩諮商心理師」與新版網站圖示；若 2-4 週仍無變化，重新做首頁 Live Test 與 favicon 可抓取性檢查。
- [ ] 發布後檢查 `https://yuchienpsy.com/talks.html` 是否顯示新版講座紀錄與合作主題。
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
- [x] 建立「更新講座紀錄與講座邀約頁」工作流。
- [ ] 之後每次新增文章都同步更新文章列表、系列頁、sitemap、meta 與 canonical。
- [ ] 之後每次修改服務資訊都同步檢查首頁、CTA、LINE 連結與手機版。
- [ ] 之後每次更新 `講座紀錄.csv`，都同步更新 `talks.html` 的代表合作紀錄與主題分類。
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
