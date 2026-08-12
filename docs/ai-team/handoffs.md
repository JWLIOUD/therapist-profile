# 各 AI 工作交接

更新日期：2026-07-30

## 交接制度

交接不是摘要，而是任務責任正式移轉。每次交接必須符合 `docs/maintenance-workflow.md` 的任務狀態與閘門，並留下足以讓接手角色不需猜測即可繼續工作的資訊。

### 必填格式

```text
任務 ID：
任務名稱：
目前狀態：
交接日期／時區：
交接來源：
接手角色：

目標與成功標準：
已確認決策：
不可改變事項：

已完成：
已修改檔案：
驗證證據：

尚未完成：
已知風險：
需要使用者決定：

接手角色下一步：
接手完成條件：
```

### 狀態用詞

- `intake`：已收到，尚未完成範圍確認。
- `scoped`：目標、範圍、限制與角色已確定。
- `assigned`：總管需求單已派工。
- `in_progress`：執行中，尚未進入驗收。
- `review`：等待專責或品質檢查。
- `user_preview`：等待使用者檢視或決定。
- `approved`：使用者已核准指定範圍。
- `published`：已發布，但正式站／外部驗收未必完成。
- `verified`：適用驗收有證據通過。
- `blocked`：缺少必要決策、權限或資料，無法安全前進。
- `closed`：交付、驗證、風險與下一步均已記錄。

### 證據規則

- 「已修改」附檔案與 diff 範圍。
- 「已驗證」附指令、結果、預覽網址、截圖或報告。
- 「已發布」附 commit、分支、部署結果與正式 URL。
- 「Google 已完成」需區分網站端、Search Console 與實際 SERP。
- 未執行或無法確認的項目標示「未驗證」，不得省略。

### 退回與重交

- 審查不通過時，接手角色將任務退回原負責角色，列出問題、證據與重測條件。
- 修正後建立新的交接紀錄，不覆蓋先前失敗證據。
- 品質檢查角色若自行修改問題，不得直接自我核准；由總管安排另一輪檢查。
- 使用者的新決定若改變範圍，總管需更新需求單並重新派工。

## 交接紀錄

### 2026-06-19：建立網站維護系統

- 任務名稱：建立網站總管 AI 與維護文件
- 交接來源：網站總管 AI
- 接手角色：全部角色
- 目前狀態：進行中
- 已改檔案：
  - `AGENTS.md`
  - `docs/maintenance-workflow.md`
  - `docs/ai-team/ai-roles.md`
  - `docs/ai-team/handoffs.md`
  - `docs/meetings/meeting-notes.md`
  - `docs/todos/latest-todos.md`
  - `docs/workflows/new-article.md`
  - `docs/workflows/update-service-info.md`
  - `docs/workflows/pre-publish-check.md`
  - `docs/seo/seo-audit-2026-06-19.md`
- 尚未完成：
  - 你確認服務資訊是否有要修改的新版內容。
  - 你提供下一篇要新增的文章內容。
  - 你提供 Google Search Console 狀態截圖或權限後，可進一步確認索引原因。
- 驗證方式：
  - 本機首頁與文章列表回應 `200`。
  - 檢查 `robots.txt`、`sitemap.xml`、canonical、meta robots。
- 最新驗證結果：
  - sitemap URL 數量為 32。
  - 文章頁數量為 25。
  - 25 篇文章都已列入 sitemap。
  - sitemap 內頁面都可對應到本地檔案。
  - sitemap 內頁面皆為 `index, follow`。
  - sitemap 內頁面的 canonical 皆與 sitemap URL 一致。
- 風險：
  - Google 搜尋目前查不到文章頁，可能是尚未索引、Search Console 未提交、網站權重低、或 Google 尚未處理新 sitemap。

### 2026-06-19：正式站連線檢查卡住現象

- 任務名稱：SEO 正式站可抓取性檢查
- 交接來源：網站總管 AI
- 接手角色：SEO / 發布維護 AI、品質檢查 AI
- 目前狀態：已確認此檢查方式需要避開
- 現象：
  - 執行類似以下指令時，使用者端觀察到容易卡住或等待過久：
    - `Invoke-WebRequest -Uri https://yuchienpsy.com/sitemap.xml -UseBasicParsing | Select-Object StatusCode,Content`
  - `robots.txt` 曾成功回應 `200`。
  - `sitemap.xml` 曾成功回應 `200`，但輸出 `Content` 會把整份 XML 印出，容易造成等待與干擾。
- 判斷：
  - 問題不一定是網站本身錯誤，比較像是檢查方式輸出過大、網路查詢不穩、或 sandbox/外部命令等待造成的工作流卡點。
- 後續規則：
  - 不要再用 `Select-Object StatusCode,Content` 檢查正式站大型 HTML 或 sitemap。
  - 檢查 sitemap 只取狀態碼與內容長度。
  - 檢查文章頁只取狀態碼、標題、robots、canonical，不輸出整頁 HTML。
  - 每個正式站請求都要設定 timeout，並一次只查必要 URL。
  - 若正式站查詢連續不穩，先完成本地檔案 SEO 檢查，再把 Search Console 操作交給使用者登入執行。
- 建議替代指令：
  - `Invoke-WebRequest -Uri https://yuchienpsy.com/sitemap.xml -UseBasicParsing | Select-Object StatusCode,@{Name='Length';Expression={$_.Content.Length}}`
  - `Invoke-WebRequest -Uri https://yuchienpsy.com/articles/addiction-01.html -UseBasicParsing | Select-Object StatusCode,@{Name='Length';Expression={$_.Content.Length}}`

### 2026-06-19：Google 找不到文章頁的並行檢查與修正

- 任務名稱：文章頁索引問題初步處理
- 交接來源：網站總管 AI
- 接手角色：SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 正式站檢查結果：
  - DNS 正常指向 GitHub Pages IP。
  - `https://yuchienpsy.com/robots.txt` 回 `200`，內容允許抓取。
  - `https://yuchienpsy.com/sitemap.xml` 回 `200`，正式站 sitemap 有 32 個 URL。
  - `https://yuchienpsy.com/articles/addiction-01.html` 回 `200`。
  - Googlebot User-Agent 讀取文章頁同樣回 `200`。
  - 代表文章頁 robots 為 `index, follow`。
  - 代表文章頁 canonical 為自己的正式 URL。
  - 正式站 sitemap 內 32 個 URL 全部回 `200`。
- Google 可見性：
  - `site:yuchienpsy.com/articles...` 類查詢未看到文章頁結果。
  - 目前判斷不是 robots、sitemap、404、noindex 或 canonical 錯誤造成。
- 找到的可改善項：
  - 首頁原本沒有直接連到文章頁。
  - 首頁心理專欄區塊有兩個系列仍顯示「即將開放」並連到 `#`，但系列頁已存在。
- 已修正：
  - `index.html` 新增 3 篇精選文章直接連結。
  - `index.html` 將職場與界線系列入口改為實際系列頁。
  - `styles.css` 新增精選文章連結樣式。
  - `sitemap.xml` 首頁 `lastmod` 更新為 `2026-06-19`。
- 驗收結果：
  - 本機首頁回 `200`。
  - 首頁直接文章連結數：3。
  - 首頁心理專欄區塊不再有 `href="#">即將開放`。
  - sitemap 32 個 URL 仍都能對應到本地檔案。
- 下一步：
  - 需要使用者登入 Google Search Console，檢查文章 URL Inspection 的實際索引原因。

### 2026-06-30：講座邀約 SEO 任務

- 任務名稱：將「講座合作」改為「講座邀約」並建立 SEO 目標頁
- 交接來源：網站總管 AI
- 接手角色：內容編輯 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 目前狀態：本地修改完成，待發布與 Search Console 驗證
- 已改檔案：
  - `index.html`
  - `articles.html`
  - `talks.html`
  - `sitemap.xml`
  - `docs/meetings/meeting-notes.md`
  - `docs/seo/seo-audit-2026-06-19.md`
  - `docs/todos/latest-todos.md`
  - `docs/workflows/update-service-info.md`
  - `docs/ai-team/handoffs.md`
- 策略：
  - `talks.html` 不再作為 noindex 舊轉址頁。
  - `talks.html` 改為可索引 landing page，主打「心理師講座邀約」。
  - 首頁與文章頁導覽改連 `talks.html`，提高內部連結權重。
- 發布後驗收：
  - `https://yuchienpsy.com/talks.html` 回 `200`。
  - robots 為 `index, follow`。
  - canonical 為 `https://yuchienpsy.com/talks.html`。
  - sitemap 包含 `https://yuchienpsy.com/talks.html`。
  - Search Console URL Inspection live test 通過後，要求建立索引。

### 2026-07-05：正式採用 A 暖印章「郁」作為全站搜尋結果圖示

- 任務名稱：將 A 暖印章「郁」正式推上線，作為全站所有分頁的 favicon / Google 搜尋結果圖示來源。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者決策：
  - 直接使用最一開始的 A 暖印章「郁」版本。
  - 要正式推上線，讓 Google 搜尋結果中網站所有分頁都顯示這個圖示。
- AI 團隊分工：
  - 品牌素材 AI：將 `assets/logo-options/option-1-warm-seal-yu.png` 輸出為正式 favicon 套件。
  - SEO / 發布維護 AI：確認首頁 structured data `logo` 指向 `https://yuchienpsy.com/assets/site-icon-512.png`，所有公開 HTML 都有 favicon links。
  - 前端維護 AI：補齊文章頁與系列頁 favicon links，讓每個分頁明確使用同一組圖示。
  - 品質檢查 AI：確認 PNG 尺寸、diff 範圍、全站連結、正式站圖示檔 200。
- 已替換正式檔案：
  - `favicon.ico`
  - `assets/site-icon-512.png`
  - `assets/favicon-192.png`
  - `assets/favicon-48.png`
  - `assets/apple-touch-icon.png`
- 已補強：
  - 所有公開 HTML 分頁都已明確加入 `/favicon.ico`、`/assets/favicon-48.png`、`/assets/favicon-192.png`、`/assets/apple-touch-icon.png`。
- 待發布後驗收：
  - 2026-07-05 已推送 commit `5ccbba4`。
  - GitHub Pages build `28714204138` 已成功。
  - 正式站首頁、代表文章頁、代表系列頁都回 `200`，且都有 favicon links。
  - `https://yuchienpsy.com/favicon.ico` 回 `200`，大小為 57862 bytes。
  - `https://yuchienpsy.com/assets/favicon-48.png` 回 `200`，大小為 4292 bytes。
  - `https://yuchienpsy.com/assets/favicon-192.png` 回 `200`，大小為 21906 bytes。
  - `https://yuchienpsy.com/assets/apple-touch-icon.png` 回 `200`，大小為 20520 bytes。
  - `https://yuchienpsy.com/assets/site-icon-512.png` 回 `200`，大小為 41008 bytes。
  - 用 Search Console 檢查首頁與代表文章；若已要求索引、已在 Google 服務中或已編入索引，不重複 Request indexing。
  - 依發布前檢查流程做 Google 實際搜尋結果截圖驗收。

### 2026-07-05：網路參考簡單線條狗 Logo 候選

- 任務名稱：直接上網查找簡單線條狗參考，重新設計狗為主體的搜尋結果 logo 候選。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 請直接在網路上找「簡單線條狗」。
  - 用相關圖片作為模仿目標，設計簡單線條狗為主體的標示。
- 參考來源類型：
  - Depositphotos：站姿狗線條 icon。
  - Pinterest：one-line dog logo 與簡單線條狗。
  - VectorStock：圓形狗頭連續線 logo。
  - Creative Fabrica / 123RF：坐姿極簡狗、單線狗。
  - IKEA 搜尋結果中也出現幾何狗 icon 風格，可作為小尺寸清晰度參考。
- AI 團隊決策：
  - 品牌素材 AI：只取共同風格特徵，不照抄任何單一圖片。
  - SEO / 發布維護 AI：三版都保留 512x512，預覽包含 48px 小尺寸。
  - 前端維護 AI：本輪仍不替換正式 favicon。
  - 品質檢查 AI：正式 `favicon.ico` 與 `assets/site-icon-512.png` 未被改動。
- 已建立版本：
  - E1 圓框狗頭：`assets/logo-options/option-e1-circle-dog-head.png`
  - E2 坐姿一筆線狗：`assets/logo-options/option-e2-one-line-sitting-dog.png`
  - E3 站姿幾何狗：`assets/logo-options/option-e3-geometric-standing-dog.png`
  - 總覽預覽：`assets/logo-options/option-e-web-line-dog-preview.png`
- 目前狀態：
  - 等使用者選 E1 / E2 / E3，或提出微調方向。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。
  - GitHub Pages 先前曾出現 queued / `Deployment failed, try again later` 狀態，正式發布時需確認 Pages build 成功。

### 2026-07-05：Google 搜尋結果狗線條標示候選

- 任務名稱：將 Google 搜尋結果 logo 方向改為「簡單線條構成的狗」。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 不再繼續使用「郁」字作為主要候選。
  - 想改成一隻用簡單線條構成的狗作為標示主體。
- AI 團隊決策：
  - 品牌素材 AI：產生 3 個非照片、簡單線條、暖系狗圖示。
  - SEO / 發布維護 AI：三版都保留 512x512，預覽含 48px 小圖；狗的輪廓需在搜尋結果小尺寸可辨識。
  - 前端維護 AI：本輪仍不替換正式 favicon，等使用者選定 D1 / D2 / D3。
  - 品質檢查 AI：確認正式 `favicon.ico` 與 `assets/site-icon-512.png` 未被改動。
- 已建立版本：
  - D1 環抱線條狗：`assets/logo-options/option-d1-curled-line-dog.png`
  - D2 坐姿線條狗：`assets/logo-options/option-d2-sitting-line-dog.png`
  - D3 暖心線條狗：`assets/logo-options/option-d3-heart-line-dog.png`
  - 總覽預覽：`assets/logo-options/option-d-line-dog-preview.png`
- 目前狀態：
  - 等使用者選 D1 / D2 / D3，或提出微調方向。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。
  - GitHub Pages 先前曾出現 queued / `Deployment failed, try again later` 狀態，正式發布時需確認 Pages build 成功。

### 2026-07-05：A 暖印章「郁」活動墨水手寫版

- 任務名稱：依使用者追加的多張活動手寫字參考，重做 A 暖印章「郁」字，讓字感更接近講義、活動筆記、麥克筆墨水字。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 追加多張活動常見手寫墨水字參考。
  - 目標不是一般電腦字型，而是有速度、有拖筆、有一點不規則的手寫墨水字。
  - 仍要保留視覺正中心，不能偏上。
- AI 團隊決策：
  - 品牌素材 AI：A7-A9 是初步手繪稿；本輪改為保留「郁」字正確字形，再加入墨水不規則感與速度筆觸。
  - SEO / 發布維護 AI：A10-A12 都保留 512x512 與 48px 預覽，避免搜尋結果縮小後不可讀。
  - 前端維護 AI：本輪仍不替換正式 favicon。
  - 品質檢查 AI：A12 第一版偏右上，已修正置中；正式 `favicon.ico` 與 `assets/site-icon-512.png` 未變動。
- 已建立版本：
  - A10 活動墨水字：`assets/logo-options/option-a10-activity-ink-kai.png`
  - A11 俏皮墨水字：`assets/logo-options/option-a11-playful-ink-kai.png`
  - A12 飄逸墨水字：`assets/logo-options/option-a12-flowing-ink-kai.png`
  - 總覽預覽：`assets/logo-options/option-a-activity-ink-preview.png`
- 目前狀態：
  - 等使用者選 A10 / A11 / A12，或提出微調方向。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。
  - GitHub Pages 在 2026-07-05 曾出現 `Deployment failed, try again later` 與 queued 狀態，後續發布正式 favicon 時需確認 Pages build 成功。

### 2026-07-05：A 暖印章「郁」墨水手寫字版

- 任務名稱：依使用者參考圖，將 A 暖印章「郁」改為活動常見的墨水手寫字方向。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 想用活動常見的墨水手寫字體。
  - 參考圖是黑色手寫筆記風格，筆畫有速度、不像正式電腦字。
  - 文字仍要放在正中心，避免偏上造成煩躁感。
- AI 團隊決策：
  - 品牌素材 AI：不用一般電腦字型套字，改用手繪筆畫方式畫出「郁」字。
  - SEO / 發布維護 AI：三版保留 512x512，預覽包含 48px 小尺寸，避免手寫字在搜尋結果縮小後糊掉。
  - 前端維護 AI：本輪仍不替換正式 favicon。
  - 品質檢查 AI：A4-A6 視為上一輪過渡稿；目前優先候選改為 A7-A9。
- 已建立版本：
  - A7 清楚墨水字：`assets/logo-options/option-a7-ink-marker-clear.png`
  - A8 可愛麥克筆：`assets/logo-options/option-a8-ink-marker-cute.png`
  - A9 飄逸手寫字：`assets/logo-options/option-a9-ink-marker-flowing.png`
  - 總覽預覽：`assets/logo-options/option-a-ink-handwriting-preview.png`
- 目前狀態：
  - 等使用者選 A7 / A8 / A9，或提出微調方向。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。

### 2026-07-05：A 暖印章「郁」飄逸可愛置中版

- 任務名稱：依使用者回饋重做 A 暖印章字體版本，要求更飄逸可愛，且文字必須放在視覺正中心。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 想要字體更飄逸可愛。
  - 文字偏上會讓人感到煩躁。
  - 文字要放在正中心。
- AI 團隊決策：
  - 品牌素材 AI：保留 A 暖印章外框，重做 3 個更柔軟、可愛、置中的「郁」字版本。
  - SEO / 發布維護 AI：仍保留 512x512 來源圖，總覽圖包含 48px 小尺寸預覽。
  - 前端維護 AI：本輪仍不替換正式 favicon，避免未選定版本直接上線。
  - 品質檢查 AI：確認正式 `favicon.ico` 與 `assets/site-icon-512.png` 未被改動。
- 已建立版本：
  - A4 飄逸楷體：`assets/logo-options/option-a4-floating-kai-centered.png`
  - A5 柔和明體：`assets/logo-options/option-a5-soft-serif-centered.png`
  - A6 可愛圓體：`assets/logo-options/option-a6-cute-rounded-centered.png`
  - 總覽預覽：`assets/logo-options/option-a-centered-cute-variants-preview.png`
- 目前狀態：
  - 等使用者選 A4 / A5 / A6，或提出微調方向。
  - A1-A3 視為上一輪候選，不作為目前優先推薦。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。

### 2026-07-05：A 暖印章「郁」字體版本

- 任務名稱：使用者選定 A 暖印章方向後，產出 3 個更有活力的「郁」字字體版本。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者決策：
  - 已選定 A 暖印章「郁」方向。
  - 希望字體更有活力一點。
  - 仍需提供 3 個版本讓使用者選。
- AI 團隊決策：
  - 品牌素材 AI：保留暖印章外框，只調整「郁」字字體與微小角度，避免整體方向漂移。
  - SEO / 發布維護 AI：三版都維持 512x512，並檢查 48px 小尺寸。
  - 前端維護 AI：本輪不替換正式 favicon。
  - 品質檢查 AI：確認正式 `favicon.ico` 與 `assets/site-icon-512.png` 未被改動。
- 已建立版本：
  - A1 活潑明體：`assets/logo-options/option-a1-lively-serif-yu.png`
  - A2 圓潤黑體：`assets/logo-options/option-a2-rounded-sans-yu.png`
  - A3 書寫楷體：`assets/logo-options/option-a3-kai-yu.png`
  - 總覽預覽：`assets/logo-options/option-a-font-variants-preview.png`
- 目前狀態：
  - 等使用者選 A1 / A2 / A3，或提出微調方向。
  - 選定後再替換正式 favicon 套件並發布。
  - 替換並發布後需做正式站圖示檔 200 檢查、Search Console 檢查與 Google 實際搜尋結果截圖驗收。

### 2026-07-05：Google 搜尋結果小圖改版 Logo 選項

- 任務名稱：把 Google 搜尋結果中不可接受的人像縮圖，改為溫暖、正式、符合網站風格的非照片 logo。
- 交接來源：網站總管 AI
- 接手角色：品牌素材 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI
- 使用者回饋：
  - 搜尋結果的小圖片目前仍像人像照片縮圖，使用者不能接受。
  - 新圖示需溫暖系，與網站風格搭配，可以是圖案或文字，但不要直接用照片。
  - 先提供 3 個選項讓使用者選，不要未選定就直接替換正式 favicon。
- AI 團隊決策：
  - 品牌素材 AI：以網站既有色彩 `cream / almond / peach / sage / brown` 做 3 個可選圖示。
  - SEO / 發布維護 AI：三個選項都需可做 512x512 來源圖，後續可輸出 favicon 套件。
  - 前端維護 AI：本輪只新增候選圖，不改正式 `<link rel="icon">` 或正式 `site-icon-512.png`。
  - 品質檢查 AI：檢查 512x512 與 48px 預覽，避免小尺寸不可讀。
- 已建立選項：
  - A 暖印章「郁」：`assets/logo-options/option-1-warm-seal-yu.png`
  - B 傾聽心形：`assets/logo-options/option-2-listening-heart.png`
  - C YP 字標：`assets/logo-options/option-3-calm-yp.png`
  - 總覽預覽：`assets/logo-options/logo-options-preview.png`
- 說明文件：
  - `docs/brand/google-serp-logo-options.md`
- 目前狀態：
  - 等使用者選 A / B / C。
  - 選定後再替換正式 `favicon.ico`、`assets/favicon-48.png`、`assets/favicon-192.png`、`assets/apple-touch-icon.png`、`assets/site-icon-512.png`。
  - 替換並發布後，必須執行 Google 實際搜尋結果截圖驗收。

### 2026-07-04：Google 搜尋結果品牌曝光與點擊率提升專案

- 任務名稱：讓 Google 搜尋結果更像正式網站，盡量顯示「黃郁倩諮商心理師」與清楚網站圖示，而不是只顯示 `yuchienpsy.com`
- 交接來源：網站總管 AI
- 接手角色：SEO / 發布維護 AI、品牌素材 AI、前端維護 AI、品質檢查 AI、內容編輯 AI
- Google 官方判斷：
  - Google 的網站名稱與 favicon 不是 Search Console 裡手動輸入後立即生效的欄位。
  - 網站名稱主要依首頁內容、`WebSite` structured data、`og:site_name`、標題與其他首頁文字自動判斷。
  - favicon 需要首頁有 `<link rel="icon">`，且 Googlebot 與 Googlebot-Image 都能抓取首頁與圖示檔。
  - 即使網站端設定正確，Google 仍需要重新抓取與處理，通常要數天到數週。
- 問題判斷：
  - 正式站可抓取，首頁、sitemap、robots 與 favicon 不是完全失效。
  - 舊 favicon 偏向人像縮圖，在搜尋結果小尺寸顯示時品牌辨識度弱。
  - 首頁部分品牌文字有空格版本「黃郁倩 諮商心理師」，`WebSite.name` 則為無空格版本；雖非錯誤，但為了讓 Google 判斷更集中，本次統一核心訊號。
- AI 團隊決策：
  - 品牌素材 AI：建立更像網站標示的小尺寸圖示，不再只依賴人像縮圖；採用暖色底、深棕「郁」字與品牌色環，提升小尺寸辨識度。
  - SEO / 發布維護 AI：首頁 `WebSite.name`、`publisher`、品牌實體 `logo`、favicon links 全部對齊。
  - 前端維護 AI：首頁、文章列表、講座邀約頁同步 favicon link 與頁首品牌文字。
  - 品質檢查 AI：發布前後檢查圖示檔 HTTP 200、核心頁可開啟、Search Console 不重複消耗 Request indexing 額度。
- 已修改檔案：
  - `index.html`
  - `articles.html`
  - `talks.html`
  - `favicon.ico`
  - `assets/favicon-48.png`
  - `assets/favicon-192.png`
  - `assets/apple-touch-icon.png`
  - `assets/site-icon-512.png`
  - `docs/workflows/pre-publish-check.md`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 發布後驗收：
  - 2026-07-04 已推送 commit `eb57037`。
  - GitHub Pages build `28696441473` 已完成且成功。
  - `https://yuchienpsy.com/` 回 `200`，正式站首頁已包含 `site-icon-512.png` 與 `黃郁倩諮商心理師` 新訊號。
  - `https://yuchienpsy.com/favicon.ico` 回 `200`。
  - `https://yuchienpsy.com/assets/favicon-48.png` 回 `200`。
  - `https://yuchienpsy.com/assets/favicon-192.png` 回 `200`。
  - `https://yuchienpsy.com/assets/apple-touch-icon.png` 回 `200`。
  - `https://yuchienpsy.com/assets/site-icon-512.png` 回 `200`。
  - 首頁 HTML 可看到 `WebSite` name 為 `黃郁倩諮商心理師`，且 `publisher` 指向品牌實體。
  - 首頁 HTML 可看到品牌實體 `logo` 指向 `assets/site-icon-512.png`。
  - Search Console 檢查首頁時，若已在 Google 服務中、已編入索引或已要求建立索引，只做紀錄，不得重複按 Request indexing。
- 後續追蹤：
  - Google 搜尋結果品牌曝光不可只用 HTTP 200、structured data 或 Search Console 狀態驗收。
  - 必須使用實際瀏覽器搜尋 `黃郁倩心理師`、`黃郁倩諮商心理師`、`黃郁倩心理師 yuchienpsy.com`、`site:yuchienpsy.com 黃郁倩心理師`，並截圖保存搜尋結果第一頁。
  - 截圖需記錄搜尋日期、瀏覽器、關鍵字、yuchienpsy.com 結果排名、顯示網站名稱、favicon、標題與摘要。
  - 若截圖驗收未通過，先判斷是 Google 尚未重抓、索引不足、搜尋結果尚未更新，或網站端訊號仍不一致。
  - 若可由網站端修正，SEO / 發布維護 AI、前端維護 AI、品牌素材 AI 需提出下一輪修正並重新發布。
  - 若需要使用者登入 Google、操作 Search Console、判斷截圖是否符合品牌期待，網站總管 AI 必須停下與使用者討論。
  - 發布後 3-14 天觀察 Google 搜尋結果。
  - 若 2-4 週後仍只顯示網址，重新執行首頁 Live Test、favicon 檔案抓取檢查、Google rich result / structured data 檢查，並確認沒有快取或錯誤 canonical。

### 2026-06-30：Google 搜尋結果 site name 顯示任務

- 任務名稱：讓 Google 搜尋結果站名從 `yuchienpsy.com` 更有機會顯示為「黃郁倩諮商心理師」
- 交接來源：網站總管 AI
- 接手角色：SEO / 發布維護 AI、前端維護 AI、品牌素材 AI、品質檢查 AI
- 目前狀態：本地修改完成，待發布與 Google 重新抓取
- 背景：
  - 使用者截圖顯示 Google 搜尋結果上方 site name 目前為 `yuchienpsy.com`。
  - 使用者希望顯示為「黃郁倩諮商心理師」。
  - Google site name 由 Google 自動產生，不能保證立即或必然改成指定文字，但可用 structured data、`og:site_name`、首頁文字與 favicon 提供更一致訊號。
- 已改檔案：
  - `index.html`
  - `articles.html`
  - `talks.html`
  - `favicon.ico`
  - `assets/favicon-192.png`
- 已完成：
  - 首頁 `WebSite` JSON-LD `name` 改為 `黃郁倩諮商心理師`。
  - 首頁 `WebSite` JSON-LD `alternateName` 保留 `黃郁倩 諮商心理師` 與 `郁倩心理師`。
  - 首頁、文章列表頁、講座邀約頁 `og:site_name` 改為 `黃郁倩諮商心理師`。
  - 新增 root `favicon.ico`。
  - 新增 `assets/favicon-192.png`。
  - 首頁、文章列表頁、講座邀約頁加入 favicon link。
- 驗收結果：
  - 本機 `/favicon.ico` 回 `200`。
  - 首頁可看到 `WebSite` structured data name 為 `黃郁倩諮商心理師`。
  - 首頁、文章列表頁、講座邀約頁 `og:site_name` 一致。
- 發布後注意：
  - 重新提交 sitemap。
  - URL Inspection 檢查首頁 `https://yuchienpsy.com/`。
  - 若 Search Console 已顯示「已要求建立索引」、已在 Google 服務中、或已編入索引，不得再次按 Request indexing，只做紀錄，避免浪費每日額度。
  - Google 更新 site name 可能需要數天到數週，不一定會即時顯示。

### 2026-06-30：正式站仍顯示「講座合作」的原因確認

- 任務名稱：確認正式站導覽仍顯示舊詞
- 交接來源：網站總管 AI
- 接手角色：發布維護 AI、品質檢查 AI
- 目前狀態：原因已確認，待發布本地變更
- 檢查結果：
  - 本地首頁已沒有 `講座合作`。
  - 本地首頁已改為連到 `talks.html`，不再使用 `#speaking`。
  - 正式站 `https://yuchienpsy.com/` 仍有 `講座合作`。
  - 正式站仍有 `#speaking` 連結，尚未更新為 `talks.html`。
- 判斷：
  - 這不是本地檔案漏改，而是本地修正尚未發布到 GitHub Pages。
- 下一步：
  - commit 並 push `main`。
  - 等 GitHub Pages 部署完成後，重新檢查正式站首頁是否已顯示 `講座邀約`。

### 2026-06-30：講座紀錄轉為講座邀約頁

- 任務名稱：將 `講座紀錄.csv` 潤色為公開講座邀約頁
- 交接來源：網站總管 AI
- 接手角色：內容文案 AI、SEO / 發布維護 AI、前端與風格圖 AI、品質檢查 AI
- 原始資料：
  - `講座紀錄.csv`
  - 內容包含 2024-2025 近年合作單位、講座主題與部分內部行政欄位。
  - 此檔案已加入 `.gitignore`，只作為本機內部維護資料，不應發布到 GitHub Pages。
- 內容決策：
  - 公開頁不呈現內部行政資料。
  - 不做完整流水帳表格，避免行政窗口與潛在個案閱讀負擔過高。
  - 不使用 `60+`、`5 類` 這類數字摘要作為主宣傳，避免被誤解為合作數量少或只能與固定類型單位合作。
  - 整理成「合作主題能力」、「適合合作單位」、「邀約資訊」。
  - 合作單位以場域分類字卡呈現，不另外放合作紀錄表格。
  - 社區心理衛生中心歸入公部門與社區心理衛生相關場域，不獨立成一類。
  - 合作單位名稱需使用正式或較正式的公開名稱；不確定時先查證，不要用太口語的簡稱。
  - 漢聲廣播電台歸入公部門相關場域。
  - 文案同時服務兩種讀者：
    - 行政人員：快速判斷能邀約哪些主題。
    - 潛在個案：看到心理師有企業、校園、公部門、司法與社區合作經驗，形成專業信任感。
- SEO 決策：
  - `talks.html` 保持獨立可索引頁。
  - 主要關鍵字：`心理師講座邀約`。
  - 延伸關鍵字：`職場心理健康講座`、`親職講座`、`壓力調適講座`、`職場霸凌調查`、`心理健康急救`。
- 風格決策：
  - 延續網站既有溫暖、低壓、專業風格。
  - 首屏改用「依單位需求設計」、「把心理專業說得好懂」、「兼顧溫度與現場可用性」三個價值訊息。
  - 合作單位區塊改為分類字卡與單位標籤，不用橫向合作紀錄表格。
  - 不做過度商業化銷售頁，避免和心理師品牌調性衝突。
- CTA 決策：
  - 不再只使用 `mailto:`，避免手機或桌機交給錯誤 App 開啟。
  - 講座邀約按鈕以 Gmail 撰寫頁為主。
  - 點擊 Gmail 邀約時同步嘗試複製 `yuchien9489@gmail.com`。
  - 若 Gmail 被阻擋，畫面需提示 Email 已複製或提供手動寄信資訊。
- 已修改檔案：
  - `.gitignore`
  - `index.html`
  - `talks.html`
  - `styles.css`
  - `docs/ai-team/handoffs.md`
  - `docs/meetings/meeting-notes.md`
  - `docs/workflows/update-talk-records.md`
  - `docs/todos/latest-todos.md`
- 驗收方式：
  - 本機開啟 `talks.html`，確認不是轉跳頁。
  - 檢查 `talks.html` 為 `index, follow`。
  - 檢查 canonical 為 `https://yuchienpsy.com/talks.html`。
  - 檢查首頁與文章頁導覽都連到 `talks.html`。
  - 全站連結檢查需確認 `talks.html`、首頁、文章頁都回 `200` 且有內容。
### 2026-07-05：職場霸凌調查委員／外聘心理師 SEO 頁面草案

- 任務名稱：讓需要職場霸凌調查委員、申訴評議委員或安全及衛生防護委員會外聘心理師的行政窗口，能透過 Google 找到明確邀約頁。
- 使用者限制：本次只做本地預覽，不上線、不 push；需等使用者確認後再發布。
- 總管 AI 決策：
  - 不把需求只塞在 `talks.html`，因為「講座邀約」與「調查／評議／外聘委員」搜尋意圖不同。
  - 新增獨立頁 `workplace-bullying-committee.html`，主打行政窗口會搜尋的精準語句。
  - `talks.html` 保留職場霸凌與不法侵害教育訓練，但把「委員邀約」導到獨立頁。
  - `index.html` 專業背景區與講座區加入入口，讓使用者能從首頁理解此服務存在。
- AI 團隊分工：
  - 內容編輯 AI：文案站在公部門人事、政風、職安、HR、EAP 行政窗口角度，強調「可先來信評估邀約角色」，不承諾調查結論。
  - SEO / 發布維護 AI：關鍵字包含 `職場霸凌調查委員`、`職場霸凌外聘委員`、`職場霸凌心理師`、`安全及衛生防護委員會 外聘委員`、`不法侵害調查 心理師`、`公部門職場霸凌 委員`。
  - 前端維護 AI：新增頁面沿用既有 `styles.css`、Gmail CTA 與複製 Email 備援；避免新增費用資訊。
  - 品質檢查 AI：本地預覽需確認首頁、講座頁、新頁、Gmail 邀約、複製 Email、手機版導覽與 sitemap 都正常。
- 已修改檔案：
  - `workplace-bullying-committee.html`
  - `index.html`
  - `talks.html`
  - `styles.css`
  - `sitemap.xml`
- 上線前待辦：
  - 使用者本地預覽確認文案與版面。
  - 確認是否要補更多實際委員經驗或正式單位名稱。
  - 上線前執行全站連結檢查與本地瀏覽器驗收。
  - 若上線，發布後到 Search Console 檢查新 URL；若已要求建立索引、已在 Google 服務中或已編入索引，不得重複按 Request indexing。
- 本輪驗收紀錄：
  - 使用 Codex 內建 Node REPL 啟動本地靜態伺服器：`http://127.0.0.1:8011/workplace-bullying-committee.html`。
  - `Start-Process` 與本機 Python 執行受 Windows/Codex 權限限制，無法作為背景伺服器方案。
  - HTTP 檢查通過：`/`、`/talks.html`、`/workplace-bullying-committee.html`、`/sitemap.xml`、`/styles.css` 均回 200。
  - 新頁檢查通過：H1、漁業署/農糧署經驗、Gmail CTA、複製 Email、FAQ schema 均存在，且未出現費用資訊。
  - 主要頁面內部連結與錨點檢查通過，未發現空白頁或斷裂內部跳轉。
  - Playwright / 瀏覽器自動截圖受權限限制，視覺預覽需由使用者開啟本地網址確認。

### 2026-07-07：職場霸凌委員獨立頁擱置與職場心理健康 SEO 測試文

- 任務名稱：暫停上一輪職場霸凌委員獨立頁正式站導入，改做職場心理健康／職場霸凌文章 SEO 改寫內部測試版。
- 使用者最新決策：
  - `workplace-bullying-committee.html` 還需要改，暫時不要加入正式網站。
  - 先測試現有心理專欄是否可改寫成「心理健康 × 職場／社會制度」長尾關鍵字文章。
- 總管 AI 決策：
  - 將上一輪正式站入口還原：`index.html`、`talks.html`、`sitemap.xml`、`styles.css` 不保留職場霸凌委員獨立頁入口。
  - 將上一輪獨立頁草案移到 `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html`，只作為擱置素材。
  - 以現有 `articles/workplace-05.html` 作為母稿，建立內部測試文 `drafts/workplace-mental-health-seo-test.html`。
  - 測試文設定 `noindex, nofollow`，不加入 `articles.html`、系列頁或 `sitemap.xml`。
- AI 團隊分工：
  - 內容編輯 AI：把原本「黑羊效應／職場霸凌」文章改寫成更貼近職場人搜尋意圖的專欄，保留心理師溫和、科普、不診斷的語氣。
  - SEO / 發布維護 AI：聚焦長尾關鍵字 `職場心理健康`、`職場霸凌處理機制`、`心理諮商如何幫助職場人`、`職場倦怠預防`、`心理健康與工作生活平衡`、`職場性別平等與心理健康`。
  - 前端維護 AI：沿用 `article.css` 建立可預覽內部草稿，不新增正式導覽或 sitemap。
  - 品質檢查 AI：確認正式站入口已移除、測試文為 noindex、測試文 HTTP 可開啟且主要連結正常。
- 目前狀態：
  - 本次為內部測試版，不上線、不提交 Search Console。
  - 若使用者喜歡此方向，下一步才是決定要覆寫原文、另開新文，或做系列文章策略。

### 2026-07-25：建立搜尋趨勢與內容情報 AI 團隊

- 任務名稱：建立即時關鍵字、SERP 與內容機會研究團隊
- 交接來源：網站總管 AI
- 接手角色：搜尋趨勢研究 AI、SERP／搜尋意圖分析 AI、內容機會策略 AI、研究品質檢查 AI、內容編輯 AI
- 目前狀態：團隊角色、固定工作流、報告範本與第一份基準報告已建立，尚未啟用自動排程或 Search Console 資料串接。
- 已改檔案：
  - `docs/ai-team/ai-roles.md`
  - `docs/workflows/keyword-trend-research.md`
  - `docs/seo/keyword-research/report-template.md`
  - `docs/seo/keyword-research/keyword-opportunity-2026-07-25.md`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 尚未完成：
  - 使用者確認職場心理健康 SEO 測試文方向。
  - 取得 Search Console 資料後建立本站實際流量與關鍵字成效基準。
  - 決定是否建立雙週或每月自動排程。
- 驗證方式：
  - 公開來源的趨勢、政策與 SERP 訊號均與本站實際流量分開標示。
  - 報告未宣稱未取得的精確搜尋量、點擊或固定排名。
  - 研究報告只位於 `docs/`，沒有加入公開導覽或 sitemap。
- 風險或需要使用者決定：
  - Google Trends 是相對興趣，不是搜尋量；手動搜尋排名只是當下快照。
  - 自站查詢、曝光、點擊、CTR 與平均排名需要 Search Console。
  - 心理健康、法律與職場制度文章仍需專業審稿與使用者預覽。
  - 擱置頁與 SEO 測試文維持原限制，不得正式化或加入 sitemap。

### 2026-07-25：限定心理健康情報範圍與建立 SEO 語意保真發包流程

- 任務名稱：將搜尋情報轉為可控的即時 SEO 修改與網站驗收流程
- 交接來源：網站總管 AI
- 接手角色：搜尋趨勢研究 AI、內容機會策略 AI、內容編輯 AI、SEO／發布維護 AI、品質檢查 AI
- 目前狀態：流程文件已完成；尚未對正式文章執行任何趨勢驅動修改。
- 已改檔案：
  - `docs/ai-team/ai-roles.md`
  - `docs/workflows/keyword-trend-research.md`
  - `docs/workflows/seo-trend-content-update.md`
  - `docs/workflows/pre-publish-check.md`
  - `docs/seo/keyword-research/report-template.md`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 核心決策：
  - 只分析與心理健康及網站專業定位直接相關的議題；無關熱門話題在評分前排除。
  - 情報報告必須檢查既有 SEO 策略並提出修正方向。
  - 網站總管核准後建立需求單，才可發包給內容、SEO 與品質檢查角色。
  - 既有內容只允許 SEO 層面的修改，不得改變核心意思、案例意義、專業主張、結論或來源。
  - 每次修改都需先建立語意基準，再進行修改前後逐項對照。
- 驗證方式：
  - `pre-publish-check.md` 已加入趨勢證據、心理健康相關性、語意保真、關鍵字互搶、完整網站回歸與使用者預覽檢查。
  - `seo-trend-content-update.md` 已明列可修改與不可修改範圍、總管需求單及雙重驗收流程。
- 風險或需要使用者決定：
  - 如果 SEO 目標無法在不改變原意的情況下完成，必須改為新增獨立文章或持續觀察。
  - 即時性不能取代專業審稿與使用者確認。
  - 未取得 Search Console 前仍不能宣稱本站真實流量或固定排名。

### 2026-07-25：重寫總管工作流、AI 角色與交接制度

- 任務 ID：`OPS-20260725-01`
- 任務名稱：統一網站總管派工、角色權責、交接與驗收規範
- 目前狀態：`verified`
- 交接日期／時區：2026-07-25／Asia/Taipei
- 交接來源：網站總管 AI
- 接手角色：品質檢查 AI
- 目標與成功標準：
  - 每個 AI 角色具有明確輸入、責任、交付、禁止事項與完成條件。
  - 每條工作流具有觸發、需求單、角色順序、交接、驗收及停止條件。
  - 交接狀態與證據格式一致。
- 已確認決策：
  - 趨勢研究限心理健康相關議題。
  - 趨勢 SEO 更新不得改變既有內容核心意義。
  - 總管建立需求單後才能派工；使用者核准後才能發布。
- 不可改變事項：
  - 正式網站內容與 sitemap 本次不修改。
  - 擱置頁與 SEO 測試文維持既有隔離規則。
- 已完成：
  - 重寫總管作業制度、AI 角色檔與全部專用工作流。
  - 更新發布前檢查與交接制度。
- 已修改檔案：
  - `docs/maintenance-workflow.md`
  - `docs/ai-team/ai-roles.md`
  - `docs/ai-team/handoffs.md`
  - `docs/workflows/*.md`
- 驗證證據：
  - `git diff --check` 通過。
  - 六份 `docs/workflows/*.md` 均存在，工作流路由與引用名稱一致。
  - 角色、需求單、交接狀態、發布閘門與停止條件已交叉核對。
  - `index.html`、`articles.html`、`talks.html`、文章、系列、CSS、`robots.txt` 與 `sitemap.xml` 本次均無 diff。
  - 擱置頁、SEO 測試文 `noindex, nofollow` 與禁止推送 `main` 規則仍保留。
- 尚未完成：
  - 使用者確認。
- 已知風險：
  - 文件規則完整不代表自動排程已啟用；自動化仍需另行授權。
- 需要使用者決定：
  - 是否在文件驗收後 commit 並推送接手分支。
- 接手角色下一步：
  - 驗證所有工作流名稱、角色名稱、狀態與限制一致；確認公開網站無 diff。
- 接手完成條件：
  - `git diff --check` 通過，所有工作流文件存在，公開網站與 sitemap 無改動。

### 2026-07-25：建立 Search Console 搜尋成效回饋閉環

- 任務 ID：`SEO-PERF-20260725-01`
- 任務名稱：將索引驗收與 Search Console 流量數據回饋趨勢及 SEO 文案團隊
- 目前狀態：`verified`
- 交接日期／時區：2026-07-25／Asia/Taipei
- 交接來源：網站總管 AI
- 接手角色：品質檢查 AI
- 目標與成功標準：
  - 有專責角色管理 sitemap、URL 索引狀態與已送出索引申請。
  - Search Console 的 query、page、click、impression、CTR、average position 能回饋趨勢與 SEO 文案策略。
  - 趨勢策略與文案目標具有可重現的發布後判定方式。
- 已確認決策：
  - Search Console 平均排名不是固定名次。
  - 讀取與分析可作驗收；提交 sitemap、Live Test 或 Request indexing 需使用者授權。
  - 不重複對已申請、已在 Google 服務中或已編入索引的 URL 送出申請。
- 不可改變事項：
  - 本次只建立制度與報告範本，不假裝已取得 Search Console 資料。
  - 正式網站內容與 sitemap 不修改。
- 已完成：
  - 新增搜尋成效與索引驗收 AI。
  - 新增 Search Console 索引／成效回饋工作流與報告範本。
  - 將回饋接入趨勢研究、SEO 更新、發布後檢查與待辦。
- 已修改檔案：
  - `docs/maintenance-workflow.md`
  - `docs/ai-team/ai-roles.md`
  - `docs/workflows/search-performance-feedback.md`
  - `docs/seo/search-performance/report-template.md`
  - `docs/workflows/keyword-trend-research.md`
  - `docs/workflows/seo-trend-content-update.md`
  - `docs/workflows/pre-publish-check.md`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 驗證證據：
  - `git diff --check` 通過。
  - `search-performance-feedback.md` 與 Search Console 報告範本存在。
  - 總管路由、角色鏈、趨勢研究、SEO 更新與發布後檢查均已引用成效回饋流程。
  - Search Console 唯讀分析、外部操作授權、重複 indexing 防護與低樣本判斷規則一致。
  - 正式 HTML、CSS、文章、`robots.txt` 與 `sitemap.xml` 本次均無 diff。
- 尚未完成：
  - 使用者確認與第一份真實 Search Console 報告。
- 已知風險：
  - 沒有 Search Console 權限或匯出資料時只能建立待辦，不能判斷真實成效。
  - 新頁 7 天資料可能過少，不能過早判定策略失敗。
- 需要使用者決定：
  - 後續以登入權限、CSV 匯出或截圖何種方式提供 Search Console 資料。
- 接手角色下一步：
  - 確認工作流、角色、報告欄位與外部操作授權邊界一致。
- 接手完成條件：
  - `git diff --check` 通過，所有引用文件存在，公開網站與 sitemap 無 diff。

### 2026-07-25：第一輪心理健康搜尋情報與三種本地 SEO 方案

- 任務 ID：`SEO-INTEL-20260725-02`
- 任務名稱：分析高機會心理健康關鍵字並建立三種網站修改方向
- 目前狀態：`approved`
- 交接日期／時區：2026-07-25／Asia/Taipei
- 交接來源：網站總管 AI
- 接手角色：使用者
- 目標與成功標準：
  - 趨勢、SERP 與內容策略團隊完成獨立分析。
  - SEO 團隊提出三種修改方向。
  - 三版只在本地建立並完成桌面、手機、連結、草稿隔離與核心頁回歸。
- 已確認決策：
  - 缺 Search Console／Keyword Planner／可匯出 Trends，因此只稱高機會訊號，不稱精確高流量排行。
  - 第一優先議題為職場霸凌新制與心理安全。
  - 三種方案為 A 單篇精修、B 職場心理健康總論、C 文章群意圖分層。
- 不可改變事項：
  - 原文案例、心理觀點、結論、來源與服務界線不變。
  - 本任務不修改正式網站、不進 sitemap、不 commit、不 push、不發布。
- 已完成：
  - 分析報告、總管需求單、SEO 修改方向、三版本地預覽與評估報告。
- 已修改檔案：
  - `docs/seo/keyword-research/team-analysis-2026-07-25.md`
  - `docs/seo/keyword-research/seo-directions-2026-07-25.md`
  - `docs/seo/keyword-research/three-options-evaluation-2026-07-25.md`
  - `docs/ai-team/requests/SEO-INTEL-20260725-02.md`
  - `drafts/seo-options/*.html`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 驗證證據：
  - 三方案及入口 HTTP `200`，桌面與 375px 手機無水平溢位。
  - 瀏覽器 console 無 warning／error，所有相對連結指向存在檔案。
  - 四個預覽頁均為 `noindex, nofollow`。
  - 首頁、文章列表、講座頁、原文章與職場系列頁回歸 `200`。
  - 正式頁面、CSS、robots 與 sitemap 無修改。
- 尚未完成：
  - 使用者選擇；任何正式改站與 Search Console 成效驗證。
- 已知風險：
  - B 與系列頁可能互搶廣義詞；C 多頁同批修改不易歸因。
- 需要使用者決定：
  - 選 A、B、C，或採分階段 A → C → B。
- 接手角色下一步：
  - 開啟本地預覽入口，閱讀評估並選擇正式候選。
- 接手完成條件：
  - 使用者明確核准下一輪範圍；總管另建正式需求單。

### 2026-07-25：方案 B 職場心理健康導航頁正式候選

- 任務 ID：`SEO-CONTENT-20260725-03`
- 任務名稱：建立職場心理健康總論與文章導航頁
- 目前狀態：`user_preview`
- 交接日期／時區：2026-07-25／Asia/Taipei
- 交接來源：網站總管 AI
- 接手角色：使用者
- 目標與成功標準：
  - 建立「職場心理健康」廣義主題入口，依七種處境導向既有文章。
  - 首頁、文章列表與職場系列頁建立自然入口。
  - 不修改任何既有文章的原意、正文、標題、案例、結論或來源。
- 已確認決策：
  - 新頁使用 `/workplace-mental-health.html`。
  - 新頁負責總論與導航；系列頁、霸凌文章、講座頁維持不同搜尋意圖。
  - 本輪只做本地候選與驗收，不發布。
- 不可改變事項：
  - 新頁維持 `noindex, nofollow`、不設正式 canonical、不進 sitemap。
  - 不 commit、不 push、不發布；尤其不得推送 `main`。
  - 擱置草案與既有 SEO 測試文不得轉為正式網站內容。
- 已完成：
  - 新頁、專用 CSS、三個站內入口、結構化資料、專屬桌機／手機插畫與本地完整驗收。
- 已修改檔案：
  - `workplace-mental-health.html`
  - `workplace-mental-health.css`
  - `index.html`
  - `articles.html`
  - `series/workplace.html`
  - `docs/ai-team/requests/SEO-CONTENT-20260725-03.md`
  - `docs/seo/keyword-research/workplace-guide-local-qa-2026-07-25.md`
  - `docs/todos/latest-todos.md`
  - `docs/ai-team/handoffs.md`
- 驗證證據：
  - `git diff --check` 通過；七篇原文章沒有 diff。
  - 單一 H1、七張導航卡、兩段 JSON-LD 可解析、相對連結無遺失。
  - 新頁維持 `noindex, nofollow`，未加入 sitemap。
  - 所有範圍內頁面與 CSS 回應 `200`；桌機與 390px 手機無水平溢位。
  - 桌機載入 1600×900 專屬導航插畫、手機載入另行構圖的 900×900 版本；alt、尺寸與裁切均通過。
  - 新頁色票已使用全站 CSS 變數；社群預覽改用專屬 1600×900 JPG。
- 尚未完成：
  - 使用者預覽與正式發布核准。
  - 發布版 robots、canonical、`og:url`、結構化資料 URL、sitemap 與 Search Console。
- 已知風險：
  - 缺少 Search Console 真實基準，現在不能證明流量成長。
  - 若未來讓導航頁與系列頁使用過度相似內容，可能發生搜尋意圖重疊。
- 需要使用者決定：
  - 是否核准此候選進入正式發布流程。
- 接手角色下一步：
  - 預覽 `/workplace-mental-health.html`，確認文案、七篇導流順序與 CTA。
- 接手完成條件：
  - 使用者明確核准或提出修正；總管依結果建立後續需求單。

### 2026-07-29：方案 B 四重驗收與正式發布授權

- 任務 ID：`SEO-CONTENT-20260725-03`
- 目前狀態：`approved`
- 交接來源：使用者／網站總管 AI
- 接手角色：SEO／發布維護 AI
- 使用者決策：
  - 通過文案、風格、網站架構與 SEO 四重驗收迴圈後正式發布。
- 驗收結果：
  - 文案：第一輪 PASS。
  - 視覺：第一輪 FAIL；修正手機首屏閱讀順序與品牌色後第二輪 PASS。
  - 網站架構：PASS。
  - SEO：第一輪 FAIL；完成正式索引設定與 sitemap 後第二輪 PASS。
- 發布候選：
  - `workplace-mental-health.html`
  - `workplace-mental-health.css`
  - `assets/illustrations/ill-007-workplace-guide-*`
  - 首頁、文章列表與職場系列頁入口。
- 保持不變：
  - 七篇文章正文、案例、標題、觀點與來源。
  - 擱置草案及既有 SEO 測試文。
- 驗證證據：
  - `docs/seo/keyword-research/workplace-guide-release-qa-2026-07-29.md`
  - `git diff --check`、JSON-LD、XML、相對連結、桌機／390px 手機與本地 HTTP 檢查通過。
- 發布後要求：
  - 驗證正式 URL、三個圖片、robots、canonical、OG、JSON-LD、sitemap 與三個 inbound。
  - 建立 Search Console 7／28／90 天回饋；外部 indexing 操作遵守授權與防重複規則。

### 2026-07-29：方案 B 正式發布完成

- 任務 ID：`SEO-CONTENT-20260725-03`
- 目前狀態：`verified`
- PR：`https://github.com/JWLIOUD/therapist-profile/pull/1`
- main commit：`9c3b35b97508b827f4245ff5c4f6b950381d41c5`
- GitHub Pages：`built`
- 正式 URL：`https://yuchienpsy.com/workplace-mental-health.html`
- 正式驗收：
  - 新頁、CSS、三個插畫、首頁、文章列表與職場系列頁均為 HTTP `200`。
  - 線上 robots、canonical、OG URL、WebPage／Breadcrumb JSON-LD 與 sitemap 通過。
  - 桌機與 390×844 手機無水平溢位、無壞圖、無 console warning／error。
  - 首頁、心理專欄與職場系列的三個導流入口均可用。
- 保持不變：
  - 七篇文章正文與原意未修改。
  - 草稿維持 noindex，未加入 sitemap。
- 接手角色下一步：
  - 搜尋成效與索引驗收 AI 依權限讀取 Search Console URL 狀態。
  - 若已送出、已在 Google 服務中或已編入索引，不重複 Request indexing。
  - 在 7／28／90 天建立 query、page、click、impression、CTR 與 average position 回饋。

### 2026-07-29：啟用每日關鍵字研究與週日 SEO 週報

- 任務名稱：心理健康關鍵字流量變化週期研究
- 目前狀態：`active`
- 排程：每日 09:00，`Asia/Taipei`
- 執行方式：
  - 週一至週六：每日心理健康相關關鍵字、搜尋意圖與本站頁面關聯研究。
  - 每週日：加做過去七日彙整，交 SEO 文案、網站風格／插畫、前端／網站架構與品質檢查組進行可行性研究。
- 週日交付：
  - 0 至 3 個修改方案及不修改／持續觀察選項。
  - 每案的目標 URL、原意保真、SEO、視覺、架構、風險與預期指標。
  - 網站總管推薦順序，提交使用者審核。
- 權限限制：
  - 自動排程只研究與提案，不得修改網站、commit、push 或發布；Search Console 的 sitemap 提交與單次 Request indexing 僅依 2026-07-29 後續授權及防重複規則執行。
  - 使用者接受方案後才開需求單與開發。
  - 文案、風格、網站架構、SEO、組織合作與講座邀約視角五重驗收均有逐輪證據，並取得使用者發布核准後，才可正式上線。

### 2026-07-29：擴充每日 Search Console 索引管理

- 任務名稱：全站 Google Search Console 索引盤點與申請佇列
- 目前狀態：`active`
- 排程：合併至每日 09:00（Asia/Taipei）總管排程。
- 使用者授權：
  - 檢查正式 sitemap 與所有可索引 URL。
  - 提交尚未存在且網站端驗證通過的正式 sitemap。
  - 對尚未申請、未處理、未在 Google 服務中、未建立索引且 Live Test 通過的正式 URL，執行單次 Request indexing。
- 每日紀錄：
  - HTTP、robots、canonical、sitemap、Google-selected canonical、索引狀態、最後檢查／申請時間、sitemap 參照與錯誤類型。
- 防重複與停止條件：
  - 已申請、處理中、已在 Google 服務中或已建立索引不得重複申請。
  - 遇到每日額度、頻率限制、CAPTCHA、登入或權限問題立即停止，保留佇列到次日。
  - 草稿、noindex、非 canonical、重複頁或網站端預檢失敗的 URL 不得送出。
- 網站修正：
  - Google 建議若需要修改 HTML、內容、canonical、robots、sitemap、結構化資料或架構，只能建立報告與方案。
  - 使用者接受方案後才進入開發、五重驗收迴圈與正式發布流程。

### 2026-07-29：首頁新增職場心理健康指南主要入口

- 任務 ID：`SEO-CONTENT-20260729-05`
- 目前狀態：`user_preview`
- 已完成：
  - 首頁「咖啡哪有工作苦」卡片以主要按鈕連到正式職場心理健康指南。
  - 保留「查看完整職場系列」次要入口。
  - 舊制文案、風格、網站架構與 SEO 四重本地驗收全部 PASS；依 2026-07-29 新制仍需補第五關及逐輪紀錄。
- 保持不變：
  - 指南正文、七篇職場文章及首頁其他內容的表達原意。
  - robots、canonical、sitemap、JSON-LD 與草稿隔離設定。
- 驗收證據：
  - `docs/seo/keyword-research/home-workplace-guide-cta-qa-2026-07-29.md`
  - 桌機 1280 × 720、手機 390 × 844、實際連結點擊與 console 檢查通過。
- 下一位接手：
  - 使用者先預覽 `http://127.0.0.1:8014/index.html#articles-entry`。
  - 僅在使用者明確核准上線後，發布維護 AI 才可 commit、push、合併與部署，再執行正式站回歸驗收。

### 2026-07-29：網站驗收制度升級為五重驗收迴圈

- 任務名稱：新增組織合作與講座邀約視角
- 目前狀態：`user_preview`
- 使用者決策：
  - 未來驗收需增加企業主管、人資／人才發展／員工關係及公部門承辦科員視角。
  - 內容應保持中立、兼顧個人與團隊影響，並支持可信任的講座合作評估。
  - 不得只有通過結論；五關都要留下明確回饋、修改前後與複驗紀錄。
- 已更新：
  - `docs/maintenance-workflow.md`
  - `docs/ai-team/ai-roles.md`
  - `docs/ai-team/five-review-log-template.md`
  - `docs/workflows/pre-publish-check.md`
  - `docs/workflows/keyword-trend-research.md`
  - `docs/workflows/seo-trend-content-update.md`
  - `docs/workflows/search-performance-feedback.md`
- 新制五關：
  - 文案與語意保真。
  - 視覺風格與無障礙。
  - 網站架構與互動。
  - SEO 與索引邊界。
  - 組織合作與講座邀約視角。
- 邊界：
  - 中立不代表偏袒雇主、淡化權力不對等或犧牲個人心理安全。
  - 商業邀約目標不得凌駕倫理、事實及必要風險說明。
- 對進行中任務的影響：
  - `SEO-CONTENT-20260729-05` 從 `user_preview` 退回 `review`。
  - 舊制四重驗收證據保留，但不得直接發布；需補第五關與完整逐輪紀錄。
- 下一步：
  - 以新範本補驗首頁職場心理健康指南入口。
  - 五重驗收完整後再交使用者預覽與核准。

### 2026-07-29：首頁指南入口完成五重驗收並取得發布核准

- 任務 ID：`SEO-CONTENT-20260729-05`
- 目前狀態：`verified`
- 使用者決策：明確回覆「核准上線」。
- 五重驗收：
  - 文案與語意保真：PASS；原卡片與指南正文未改。
  - 視覺風格與無障礙：初審 FAIL；R1 修正對比與觸控高度後複驗 PASS。
  - 網站架構與互動：PASS；桌機／手機、唯一連結、實際點擊與 console 回歸通過。
  - SEO 與索引邊界：PASS；自然 anchor，索引設定與草稿邊界未變。
  - 組織合作與講座邀約視角：PASS；企業主管、人資與公部門承辦均有逐項回饋。
- 完整紀錄：`docs/seo/keyword-research/home-workplace-guide-cta-qa-2026-07-29.md`
- 保持不變：指南正文、七篇文章、首頁其他文案、robots、canonical、sitemap、JSON-LD 與草稿隔離。
- 發布結果：
  - 使用者已重新完成 GitHub CLI 與 SSH 登入。
  - PR #5 已合併：`https://github.com/JWLIOUD/therapist-profile/pull/5`
  - main merge commit：`6277aa3e21cdd18b91ca5b50893878de0349b2f7`
  - GitHub Pages build：`built`
  - 正式首頁、指南、系列與樣式檔均為 HTTP `200`。
  - 桌機／手機、唯一入口、實際點擊、H1、canonical 與 console 回歸通過。
- 後續觀察：
  - 依既有 Search Console 工作流觀察首頁 → 指南及指南 → 講座合作的實際成效。

### 2026-07-29：全站心理專欄新增職場心理健康下拉入口

- 任務 ID：`SEO-CONTENT-20260729-06`
- 目前狀態：`verified`
- 使用者決策：
  - 不採獨立第八個頂層連結。
  - 桌機滑鼠移到「心理專欄」時顯示「職場心理健康」下拉提示。
  - 手機以縮排子項呈現。
- 版本紀錄：
  - V1 視覺 FAIL：獨立頂層入口在臨界寬度有擁擠風險。
  - V2 視覺 FAIL：短螢幕手機選單無可視高度與捲動。
  - V3 PASS：完成首頁／講座頁 1120px 桌機斷點、手機捲動、收合焦點隔離及裝飾箭頭無障礙修正。
  - V4 FAIL：擴大至全站後發現手機入口只有 2/34，且有兩處 `aria-current` 語意錯誤。
  - V5 PASS：桌機 dropdown、hamburger、mobile menu 與手機子項均為 34/34；current 語意、nowrap、快取版本、共用 CSS／JS 及產生器均完成修正與複驗。
- 五重驗收：文案、視覺／無障礙、架構／互動、SEO、組織合作／講座邀約均 PASS。
- 證據：`docs/seo/keyword-research/home-workplace-nav-five-review-2026-07-29.md`
- 保持不變：首頁、文章、系列、指南與講座正文，canonical、robots、sitemap、JSON-LD 與草稿隔離。
- 下一步：
  - 使用者已於 2026-07-30 明確核准上線。
  - PR #7 已合併至 main，GitHub Pages 部署成功。
  - 正式站桌機鍵盤下拉、390 × 568 手機選單、實際指南跳轉、無溢位／壞圖及 console 回歸均通過。

### 2026-07-30：職場心理健康指南搜尋發現性補強

- 任務 ID：`SEO-CONTENT-20260730-07`
- 目前狀態：`verified`
- 交接來源：網站總管 AI
- 接手角色：使用者；核准後交 SEO／發布維護 AI
- 目標與成功標準：
  - 讓 Google 可透過全站導覽及 sitemap 發現正式指南。
  - 讓搜尋／Discover 可使用符合條件的大型預覽圖，但不得保證收錄、排名或推播。
- 已確認決策：
  - sitemap 中保留一筆正式指南 URL，不建立重複項目。
  - 34 個正式頁均改過重要導覽連結，故 34 筆 `lastmod` 更新為 `2026-07-30`。
  - 指南 robots 加入 `max-image-preview:large`；不改正文。
- 不可改變事項：
  - 正式內容原意、canonical、結構化資料語意及草稿隔離。
  - 不加入 meta keywords、隱藏文字或關鍵字堆砌。
- 發布前新增修正：
  - 完整掃描發現 `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html` 仍為 `index, follow`。
  - 只將該擱置草稿改為 `noindex, nofollow`；草稿正文與正式內容未改。
  - `drafts/` 與 `docs/drafts/` 共 6 個草稿複驗均為 `noindex, nofollow`。
- 驗證證據：
  - 五重驗收均 PASS。
  - sitemap XML 正常，共 34 個唯一 URL，指南一筆，草稿零筆。
  - 全站桌機／手機指南入口均為 34/34 可爬取標準 anchor。
  - 指南 canonical 正確，OG 圖為 1600 × 900，本地實頁無水平溢位。
  - 完整紀錄：`docs/seo/keyword-research/workplace-guide-google-discovery-qa-2026-07-30.md`
- 發布結果：
  - 候選 commit：`b7d66dddf7b7c184878e042199fb3c7c13710cc7`
  - PR #7：`https://github.com/JWLIOUD/therapist-profile/pull/7`
  - main merge commit：`14004977db8255f98a7bd3103312db3f6b42c303`
  - GitHub Pages run：`30471185768`，狀態 `built`／`success`。
  - 正式頁、導覽 CSS／JS、sitemap 與 OG 圖均為 HTTP `200`。
  - 正式 sitemap 34 筆、指南一筆、草稿零筆；擱置草稿 robots 為 `noindex, nofollow`。
  - 桌機與 390 × 568 手機導覽、實際跳轉、版面、圖片及 console 回歸通過。
- 尚未完成：
  - Search Console URL Inspection 與實際 Search／Discover 呈現尚未驗證。
- 已知風險：
  - Google 可自行改寫摘要、裁切圖片，也可能不收錄或不顯示 Discover。
- 使用者決定：
  - 已於 2026-07-30 明確核准此候選上線。
- 接手角色下一步：
  - Search Console 依防重複規則檢查及必要的單次索引申請。
  - 依 7／28／90 天窗口回饋 query、page、click、impression、CTR 與 average position。

### 2026-08-12：非品牌詞 SEO 修改方案交使用者審核（後續已核准）

- 任務 ID：`SEO-PLAN-20260812-08`
- 目前狀態：`approved`；使用者於 2026-08-13 接受並授權驗收後直接發布
- 交接來源：網站總管 AI／搜尋趨勢與內容機會策略
- 接手角色：使用者
- 方案：
  - 以已索引的 `articles/workplace-05.html` 承接「職場霸凌怎麼辦」非品牌意圖。
  - 核准後只製作 title、H1、description、社群／JSON-LD 描述、可見導讀與 heading 層級的本地候選。
  - 不修改正文段落、案例、心理觀點、結論、來源、CTA、圖片、URL、canonical、robots、sitemap 或其他頁面。
- 證據：
  - 2026-07-25 研究將職場霸凌／心理支持列為第一順位、信心中。
  - 目標頁目前的 description 是被省略號截斷的故事片段，未清楚說明讀者效益。
  - 2026-08-12 Search Console 顯示流量仍偏品牌詞，職場指南尚未索引；本案採單頁受控測試並避免廣義意圖互搶。
  - 當下官方搜尋結果由勞動部承接制度與申訴資訊；本站方案限定心理理解、自我保護與支持意圖。
- 完整方案：`docs/seo/keyword-research/non-brand-seo-plan-2026-08-12.md`
- 已完成：方案範圍、候選文字、原意保真、互搶控制、五重驗收、7／28／90 天觀察與回復計畫。
- 尚未完成：網站實作、本地預覽、五重驗收、Git、發布與 Search Console 成效追蹤。
- 已知風險：Search Console 尚未顯示目標 query，沒有精確搜尋量；信心只列中，不保證流量、排名或 Google 採用指定摘要。
- 不可改變事項：原文語意、案例、來源、專業界線、草稿隔離與未經核准不得發布。
- 使用者決策：已接受，總管另開正式開發需求 `SEO-CONTENT-20260813-09`。
- 接手完成條件：已完成；後續狀態由正式開發需求承接。

### 2026-08-13：非品牌詞 SEO 方案獲核准並啟動開發

- 任務 ID：`SEO-CONTENT-20260813-09`
- 目前狀態：`in_progress`
- 交接來源：使用者／網站總管 AI
- 接手角色：內容編輯 AI、SEO／發布維護 AI、前端維護 AI
- 使用者決策：接受 `SEO-PLAN-20260812-08`，並授權五重驗收通過後直接提交、推送、合併與發布。
- 目標：只讓 `articles/workplace-05.html` 承接「職場霸凌怎麼辦」的心理支持意圖。
- 在範圍內：metadata、H1、可見導讀、標題層級、H3 樣式及產生器同步。
- 不可改變：正文段落、案例、心理觀點、結論、來源、CTA、圖片、其他頁面與索引邊界。
- 分支：`agent/non-brand-workplace-bullying-seo`
- 下一步：完成靜態與瀏覽器驗收，建立五重驗收紀錄；任一關 FAIL 先修正複驗。
- 完成條件：五關證據完整、範圍乾淨，PR 合併及正式站驗證完成。

### 2026-08-13：非品牌詞 SEO 候選完成五重驗收

- 任務 ID：`SEO-CONTENT-20260813-09`
- 目前狀態：`ready_to_release`
- 候選分支：`agent/non-brand-workplace-bullying-seo`
- 五重驗收：文案／語意、視覺／無障礙、架構／互動、SEO／索引邊界、組織合作／講座邀約均 PASS。
- 主要證據：正文段落保真、單一 H1、六個 H3、38 個本地參照、七個核心頁 HTTP 200、桌機／手機無溢位與壞圖、canonical／robots／sitemap 邊界不變。
- 圖片決策：現有職場系列插畫足夠，不新增圖片。
- 完整紀錄：`docs/seo/keyword-research/workplace-05-non-brand-five-review-2026-08-13.md`
- 使用者權限：已授權驗收完畢直接提交、合併與發布。
- 接手角色下一步：網站總管 AI 以獨立 PR 合併，確認 GitHub Pages 成功，再做正式站 metadata、版面與 console 回歸。
