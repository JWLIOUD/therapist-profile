# 固定流程：發布前檢查

負責角色：品質檢查 AI、SEO / 發布維護 AI、前端維護 AI、網站總管 AI

## 觸發條件

任何準備 commit、push、部署到 GitHub Pages 前都要執行。

## 檢查清單

### Git 狀態

- [ ] `git status --short --branch`
- [ ] `git diff` 只包含本次任務相關改動。
- [ ] 沒有誤加入快取、私密資料、外部 Word 檔或本機 log。

### 本機頁面

- [ ] 首頁可開啟。
- [ ] `articles.html` 可開啟。
- [ ] 至少抽查 1 篇文章頁。
- [ ] 至少抽查 1 個系列頁。
- [ ] 主要導覽可點。
- [ ] LINE CTA 可點且網址正確。
- [ ] 所有主要 CTA 按鈕可點且行為符合預期。
- [ ] Email / Gmail 類按鈕不可只依賴 `mailto:`；需確認能開啟 Gmail 撰寫頁，或至少能複製 Email 並顯示提示。

### SEO

- [ ] `robots.txt` 允許抓取。
- [ ] `sitemap.xml` URL 格式正確。
- [ ] 新增或修改的頁面有 canonical。
- [ ] 應收錄頁面為 `index, follow`。
- [ ] 不應收錄頁面為 `noindex, follow`。
- [ ] sitemap 已包含新增頁面，且未包含不應收錄頁面。

### Google 搜尋結果品牌曝光

- [ ] 首頁 `<title>`、`og:title`、`twitter:title`、頁首品牌文字使用一致網站名稱：`黃郁倩諮商心理師`。
- [ ] 首頁 `WebSite` JSON-LD `name` 為 `黃郁倩諮商心理師`，並保留 `alternateName`。
- [ ] 首頁 `WebSite` JSON-LD 有 `publisher`，且可連到同頁的心理師品牌實體。
- [ ] 首頁品牌實體有 `logo`，指向 `https://yuchienpsy.com/assets/site-icon-512.png`。
- [ ] 首頁與核心頁有 `/favicon.ico`、`/assets/favicon-48.png`、`/assets/favicon-192.png`、`/assets/apple-touch-icon.png`。
- [ ] favicon 圖檔為正方形，至少有 48x48 版本，且不是頻繁更換的 URL。
- [ ] 正式站 `/favicon.ico`、`/assets/favicon-48.png`、`/assets/favicon-192.png`、`/assets/site-icon-512.png` 都回 `200`。
- [ ] 發布後用 Search Console 檢查首頁。若已顯示「已要求建立索引」、已在 Google 服務中、或已編入索引，不得再次按 Request indexing，只做紀錄。
- [ ] Google 搜尋結果的網站名稱與 favicon 由 Google 自動產生；發布後需追蹤數天到數週，不能把未即時顯示視為網站端部署失敗。

### Google 實際搜尋結果截圖驗收

此項目是 Google 搜尋結果品牌曝光專案的必要驗收，不可用 HTTP 狀態碼、Search Console 狀態或 structured data 檢查取代。

- [ ] 使用實際瀏覽器開啟 Google 搜尋，不使用只回傳文字摘要的搜尋 API 作為最終驗收。
- [ ] 搜尋關鍵字 `黃郁倩心理師`，截圖保存搜尋結果第一頁。
- [ ] 搜尋關鍵字 `黃郁倩諮商心理師`，截圖保存搜尋結果第一頁。
- [ ] 搜尋關鍵字 `黃郁倩心理師 yuchienpsy.com`，截圖保存搜尋結果第一頁。
- [ ] 搜尋關鍵字 `site:yuchienpsy.com 黃郁倩心理師`，截圖保存搜尋結果第一頁。
- [ ] 截圖需能看見搜尋框關鍵字、搜尋結果標題、網址、摘要與網站圖示位置。
- [ ] 若搜尋結果有 `https://yuchienpsy.com/` 或相關文章頁，記錄其排名、顯示網站名稱、標題、摘要與 favicon 是否符合預期。
- [ ] 通過標準：品牌搜尋至少能找到 yuchienpsy.com 相關結果；結果中的網站名稱優先顯示 `黃郁倩諮商心理師` 或不再只以可疑裸網址呈現；favicon 顯示為新版網站圖示或 Google 已開始抓取新版圖示。
- [ ] 若未通過，先判斷是 Google 尚未重抓、搜尋結果尚未更新、索引不足、或網站端訊號仍不一致。
- [ ] 若未通過且可由網站端修正，SEO / 發布維護 AI 與前端維護 AI 需提出下一輪修正並重新發布。
- [ ] 若未通過但判斷是 Google 處理延遲、Search Console 權限、瀏覽器登入、或需要人工操作，網站總管 AI 必須停下與使用者討論，不得把專案標記為完成。
- [ ] 每次截圖驗收都需記錄日期、瀏覽器、搜尋地區或語系線索、使用的關鍵字與截圖檔位置。

### 內容與風險

- [ ] 心理健康內容沒有不當診斷或療效承諾。
- [ ] 法律、危機資源、醫療資訊沒有未確認更新。
- [ ] 原刊來源或引用資訊保留。

### 發布後

- [ ] 正式站首頁回 `200`。
- [ ] 正式站 sitemap 回 `200`。
- [ ] 正式站新增或修改頁面回 `200`。
- [ ] 正式站主要 CTA 按鈕可點；Email / Gmail 按鈕需確認 Gmail 連結、複製 Email 與提示訊息正常。
- [ ] 如有新增重要頁面，到 Google Search Console 要求建立索引。

### 正式站檢查注意事項

- 不要用 `Select-Object StatusCode,Content` 輸出 sitemap 或整頁 HTML，容易卡住或造成大量輸出。
- sitemap 與文章頁檢查只取狀態碼和內容長度。
- 需要檢查 HTML 細節時，先下載或讀取後只抽取 `<title>`、robots、canonical。
- 每次正式站網路檢查都要設定 timeout；若等待過久，停止該步驟，改回本地檔案檢查與 Search Console 人工確認。

## 完成標準

所有必要項目完成，或網站總管 AI 明確列出未完成項目與風險後，才可發布。若任務目標是 Google 搜尋結果品牌曝光，必須完成「Google 實際搜尋結果截圖驗收」；未完成截圖驗收時，只能標記為「網站端已完成、Google SERP 驗收待確認」，不得標記為整體完成。
