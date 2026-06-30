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
