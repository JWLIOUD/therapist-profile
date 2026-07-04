# 各 AI 工作交接

更新日期：2026-06-19

## 交接格式

每次交接都要留下：

- 任務名稱
- 交接來源
- 接手角色
- 目前狀態
- 已改檔案
- 尚未完成
- 驗證方式
- 風險或需要你決定的事項

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
