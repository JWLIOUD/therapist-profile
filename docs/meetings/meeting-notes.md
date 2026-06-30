# 會議記錄

## 2026-06-19：建立網站總管 AI 與 SEO 初步檢查

### 會議目標

建立本地網站維護環境，並建立 AI 維護團隊、工作流、待辦與交接文件。

### 已確認事項

- GitHub repo：`JWLIOUD/therapist-profile`
- 本地路徑：`C:\Users\roy81\Documents\therapist-profile`
- 正式網域：`yuchienpsy.com`
- 網站型態：GitHub Pages 靜態網站
- 技術架構：HTML、CSS、圖片素材、少量 Python 產生工具
- 本地預覽：`http://127.0.0.1:8000/`

### 決策

- 建立 1 個網站總管 AI 加 5 個執行 AI。
- 網站總管 AI 負責和你討論、拆任務、安排角色、整合結果。
- 固定工作流優先建立：
  - 新增文章
  - 修改服務資訊
  - 發布前檢查

### SEO 初步觀察

- 本地 `robots.txt` 允許搜尋引擎抓取。
- 本地 `sitemap.xml` 已包含文章頁與系列頁。
- 文章頁本地設定大多是 `index, follow`。
- Google `site:` 查詢目前找不到文章頁結果。

### 待確認

- Google Search Console 是否已驗證 `yuchienpsy.com`。
- sitemap 是否已在 Search Console 成功提交。
- Search Console 是否顯示「已探索但尚未建立索引」、「已檢索但尚未建立索引」或其他排除原因。
- 是否需要將文章頁加入首頁更多內部連結，提高文章被發現與重視程度。

### 本次固定流程執行結果

- 新增文章流程：已建立。因本次未提供新文章正文，未新增文章頁。
- 修改服務資訊流程：已建立。因本次未提供新版服務資訊，未修改正式頁面文案。
- 發布前檢查流程：已建立並先執行 SEO 相關自動檢查。

### 發布前 SEO 檢查結果

- sitemap URL 數量：32。
- 文章頁數量：25。
- 25 篇文章都已列入 sitemap。
- sitemap 內 URL 都對得到本地檔案。
- sitemap 內頁面皆為 `index, follow`。
- sitemap 內頁面的 canonical 皆與 sitemap URL 一致。
- `talks.html` 原本未列入 sitemap，當時作為 noindex 舊轉址頁處理。

### 文章索引問題處理紀錄

- 正式站 robots、sitemap、代表文章頁、Googlebot User-Agent 檢查皆未發現阻擋索引的設定。
- 正式站 sitemap 內 32 個 URL 全部回 `200`。
- 找到可改善項：首頁沒有直接連到文章頁，且部分已存在系列仍顯示「即將開放」。
- 已修正首頁內部連結：
  - 新增 3 篇精選文章直接連結。
  - 將職場與界線系列入口改為實際系列頁。
  - 更新首頁 sitemap `lastmod`。
- 剩餘關鍵步驟：登入 Google Search Console 查看 URL Inspection 的未索引原因。

## 2026-06-30：講座邀約 SEO 調整

### 會議目標

將網站中的「講座合作」統一改為「講座邀約」，並建立可支援「心理師 講座邀約」搜尋意圖的索引頁。

### 分工

- 網站總管 AI：決定 SEO 目標頁策略與工作流。
- 內容編輯 AI：將正式頁面文案統一為「講座邀約」，並自然加入「心理師講座邀約」。
- SEO / 發布維護 AI：讓 `talks.html` 從 noindex 轉為 indexable landing page，更新 canonical、meta、OG、JSON-LD 與 sitemap。
- 前端維護 AI：更新首頁與文章頁導覽，讓站內連結指向 `talks.html`。
- 品質檢查 AI：檢查舊詞殘留、sitemap 與本機頁面狀態。

### 已完成

- `talks.html` 改為可索引的「心理師講座邀約」頁。
- 移除 `talks.html` 的 noindex 與 meta refresh。
- `talks.html` canonical 改為 `https://yuchienpsy.com/talks.html`。
- 首頁、文章頁導覽改為「講座邀約」並連到 `talks.html`。
- `sitemap.xml` 新增 `https://yuchienpsy.com/talks.html`。
- 首頁與講座邀約頁 `lastmod` 更新為 `2026-06-30`。

### 待發布後處理

- 重新提交 sitemap。
- 用 Search Console URL Inspection 檢查 `https://yuchienpsy.com/talks.html`。
- 若 live test 通過，要求建立索引。

## 2026-06-30：Google site name 顯示調整

### 會議目標

讓 Google 搜尋結果中顯示於網址上方的 site name，更有機會從 `yuchienpsy.com` 改為「黃郁倩諮商心理師」。

### 決策

- 目標文字採用無空格版本：`黃郁倩諮商心理師`。
- 首頁 `WebSite` structured data 是主要調整點。
- 同步補強 `og:site_name` 與 favicon。
- 保留 `黃郁倩 諮商心理師` 作為 alternateName，避免既有品牌寫法完全消失。

### 已完成

- `index.html` 的 `WebSite` JSON-LD `name` 改為 `黃郁倩諮商心理師`。
- `index.html` 的 `WebSite` JSON-LD `alternateName` 改為陣列，包含 `黃郁倩 諮商心理師` 與 `郁倩心理師`。
- `index.html`、`articles.html`、`talks.html` 的 `og:site_name` 改為 `黃郁倩諮商心理師`。
- 新增 `favicon.ico` 與 `assets/favicon-192.png`。
- 首頁、文章列表頁、講座邀約頁加入 favicon link。

### 待發布後處理

- 檢查正式站 `/favicon.ico` 是否回 `200`。
- 用 Search Console URL Inspection 檢查首頁。
- 若首頁已是 indexed/requested/on Google，不重複 Request indexing，只紀錄。
- 等待 Google 重新抓取與更新搜尋結果顯示。

## 2026-06-30：正式站舊詞殘留確認

### 檢查結果

- 本地首頁沒有 `講座合作`。
- 本地首頁已連到 `talks.html`。
- 正式站首頁仍顯示 `講座合作`，且仍使用 `#speaking`。

### 結論

這是尚未發布造成的正式站舊版，不是本地檔案漏改。下一步要推送 GitHub，等待 GitHub Pages 更新後再驗收正式站。

## 2026-06-30：講座紀錄公開頁策略會議

### 會議目標

將 `講座紀錄.csv` 中近年合作單位與主題，整理成行政人員容易理解、潛在個案也能感受到專業可信度的講座邀約頁。

### AI 團隊討論結論

- 網站總管 AI：
  - 維持 `talks.html` 作為獨立 SEO landing page。
  - 首頁保留講座區塊，但主要任務改為導流到 `talks.html`。
- 內容文案 AI：
  - 不公開內部行政欄位。
  - 不逐筆塞滿所有 CSV 紀錄，改用代表性單位與場域分類。
  - 移除合作紀錄表格，避免頁面像履歷流水帳。
  - 移除 `60+`、`5 類` 這類量化摘要，避免被誤解為合作量或合作類型受限。
  - 文案重點放在「能合作什麼主題」、「適合什麼單位」、「曾有哪些合作場域」。
- SEO / 發布維護 AI：
  - 目標搜尋意圖為 `心理師 講座邀約`。
  - `talks.html` 要保留獨立 title、description、canonical、robots、OG 與 structured data。
- 前端與風格圖 AI：
  - 使用既有品牌色與卡片系統。
  - 首屏改用合作價值卡，不放數字卡。
  - 合作單位改用分類字卡與單位標籤，不放合作紀錄表格。
  - 社區心理衛生中心歸入公部門與社區心理衛生類。
- 品質檢查 AI：
  - 檢查舊詞 `講座合作` 是否仍出現在公開頁。
  - 檢查 `talks.html` 不再是 noindex 或 meta refresh。
  - 檢查所有導覽連到 `talks.html`。

### 已完成

- `talks.html` 移除合作紀錄表格，保留合作場域、主題分類與邀約資訊。
- 首屏三張數字卡改為三張合作價值卡。
- 新增主題分類：
  - 職場心理健康與組織支持
  - 校園、親職與兒少情緒
  - 關係界線、多元性別與人際理解
  - 藝術媒材與紓壓工作坊
  - 心理健康推廣與心理急救
  - 客製講題
- 首頁講座區塊改為導流到 `talks.html`。
- `.gitignore` 已加入 `講座紀錄.csv`，避免含內部欄位的原始資料被發布。
