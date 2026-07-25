# 最新待辦事項

更新日期：2026-07-25

## 最高優先

- [x] 使用者從 Google 搜尋結果 logo 候選中選擇 A / B / C；已選 A。
- [x] 使用者最終選擇 A 暖印章「郁」，已替換正式 favicon 套件並發布。
- [x] 發布後確認 `https://yuchienpsy.com/favicon.ico`、`https://yuchienpsy.com/assets/favicon-48.png`、`https://yuchienpsy.com/assets/favicon-192.png`、`https://yuchienpsy.com/assets/site-icon-512.png` 都回 `200` 且為 A 暖印章「郁」。
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
## 2026-07-05：職場霸凌調查委員 SEO 頁面

- [x] 建立 `workplace-bullying-committee.html` 本地草案。
- [x] 在首頁加入「職場霸凌委員」導覽與內容入口。
- [x] 在講座頁加入委員邀約分流 CTA。
- [x] 本地 sitemap 加入新 URL，等待使用者確認後再發布。
- [x] 本地 HTTP 檢查與主要內部連結檢查通過。
- [ ] 使用者本地預覽確認頁面文案、版面與服務定位。
- [ ] 上線前執行瀏覽器視覺確認與正式發布前完整檢查。
- [ ] 使用者確認後才 commit / push / 發布。
- [ ] 發布後再進 Search Console 檢查新 URL；若已要求建立索引、已在 Google 服務中或已編入索引，不得重複按 Request indexing。

## 2026-07-07：職場心理健康 SEO 改寫測試

- [x] 暫停 `workplace-bullying-committee.html` 正式站導入。
- [x] 將職場霸凌委員獨立頁草案移到 `docs/drafts/` 作為擱置素材。
- [x] 還原首頁、講座頁、sitemap、styles 中的上一輪正式站入口改動。
- [x] 建立內部測試文 `drafts/workplace-mental-health-seo-test.html`。
- [x] 測試文設定 `noindex, nofollow`，不加入正式列表與 sitemap。
- [ ] 使用者預覽測試文，決定是否採用此 SEO 改寫方向。
- [ ] 若採用，決定正式作法：覆寫原文、新增正式文章，或規劃職場心理健康文章群。

## 2026-07-25：搜尋趨勢與內容情報 AI 團隊

- [x] 建立搜尋趨勢研究、SERP／意圖分析、內容機會策略與研究品質檢查角色。
- [x] 建立固定關鍵字趨勢研究流程與報告範本。
- [x] 完成第一份搜尋趨勢與內容機會基準報告。
- [x] 將研究範圍限定為心理健康與網站專業直接相關議題。
- [x] 建立「總管需求單 → SEO 文案修改 → 語意保真 → 完整網站驗收」流程。
- [x] 發布前檢查加入趨勢證據、SEO 修正、原意保留與草稿隔離驗收。
- [x] 建立搜尋成效與索引驗收 AI、Search Console 索引台帳與成效回饋工作流。
- [x] 建立 Search Console 成效報告範本，回饋趨勢、策略、文案與 SEO 團隊。
- [ ] 使用者確認是否採用職場心理健康 SEO 測試文方向。
- [ ] 若使用者授權並提供 Search Console 資料，建立本站真實查詢、曝光、點擊、CTR 與平均排名基準。
- [ ] 取得 Search Console 權限或匯出資料後，建立第一份索引台帳與 28／90 天成效基準報告。
- [ ] 執行下一次雙週快速趨勢掃描，加入 Google Trends 台灣區 7／30／90 天比較。
- [ ] 決定是否另行建立自動排程；未取得明確授權前維持人工觸發。
