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

所有必要項目完成，或網站總管 AI 明確列出未完成項目與風險後，才可發布。
