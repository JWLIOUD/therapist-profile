# `workplace-05` sitemap `lastmod` 五重驗收紀錄

任務 ID：`SEO-MAINT-20260814-10`

需求單：`docs/ai-team/requests/SEO-MAINT-20260814-10.md`

驗收範圍：只把 `sitemap.xml` 中 `https://yuchienpsy.com/articles/workplace-05.html` 的 `<lastmod>` 從 `2026-07-30` 校正為 `2026-08-13`。

不可改變事項：文章正文、案例、標題、摘要、心理觀點、來源、免責、CTA、圖片、HTML、CSS、JavaScript、JSON-LD、canonical、robots、內部連結、其他 sitemap URL 與日期。

本地預覽：

- <http://127.0.0.1:8016/sitemap.xml>
- <http://127.0.0.1:8016/articles/workplace-05.html>

初審版本／diff 基準：`4fd7814`（`main`）→ `codex/seo-maint-20260814-10` working tree R0

目前狀態：`approved`

## 版本修改總表

| 輪次 | 日期／時區 | 來源版本 | 負責角色 | 修改檔案 | 修改前 | 修改後 | 理由 | 重測版本 |
|---|---|---|---|---|---|---|---|---|
| R0 | 2026-08-16／Asia/Taipei | `4fd7814` | SEO／發布維護 AI | `sitemap.xml` | 目標 URL `<lastmod>2026-07-30</lastmod>` | `<lastmod>2026-08-13</lastmod>` | 8 月 13 日為可驗證的重大 SEO 更新日，校正 sitemap 訊號 | working tree R0 |

## 驗證環境備註

- 第一輪靜態檢查腳本誤用 zsh 特殊變數 `path`，造成後續 `rg` 找不到並產生 34 筆偽 canonical FAIL。候選檔案沒有因此改動；改用 `page_file` 後完整重跑，34/34 對應、canonical 與 indexability 均通過。
- 沙箱內 `curl` 無法連到在主機環境啟動的本地伺服器，屬執行環境隔離，不是網站錯誤；改由同一主機環境重跑後 7 個本地 URL 全為 HTTP 200。
- 上述為驗證工具／環境失敗，沒有建立候選修正輪次，也沒有刪除或覆蓋失敗紀錄。

## 1. 文案與語意保真

### 初審

- 驗收角色：內容編輯 AI／品質檢查 AI
- 檢查版本：working tree R0
- 逐項觀察與證據：
  - `git diff --name-only -- '*.html' '*.css' '*.js' 'assets/**'` 無輸出。
  - `git diff -- sitemap.xml` 只有目標 URL 的單一日期行變更。
  - `articles/workplace-05.html` 與 `HEAD` 無 diff；title、description、H1、正文、案例、來源、免責與 CTA 均未修改。
- 原意／事實／來源對照：公開文章的核心問題、黑羊效應解釋、心理影響、自我保護觀點、結論與來源完全沿用 2026-08-13 已驗證版本。
- 風險：`lastmod` 只是一項技術提示，不得對外宣稱內容再次更新或搜尋成效已改善。
- 判定：`PASS`
- 修改指示與重測條件：無；若出現任何 HTML 或公開文案 diff，必須退回 R1 並重新做語意對照。

### 複驗

- 不適用；初審沒有候選缺陷或後續修改。

## 2. 視覺風格與無障礙

### 初審

- 驗收角色：品牌素材 AI／前端維護 AI／品質檢查 AI
- 檢查版本：working tree R0
- 桌機／手機／圖片需求／無障礙證據：
  - HTML、CSS、JavaScript 與 `assets/` diff 為 0，因此版面、響應式斷點、圖片、alt、閱讀順序、鍵盤操作與觸控區沒有候選差異。
  - 本地桌面實頁已在瀏覽器載入；頁首、導覽、H1 與既有職場插畫正常呈現。
  - 手機基準沿用 2026-08-13 已驗證的 390 × 844 結果；本輪沒有任何能改變手機顯示的檔案。
  - 圖片需求判定：不需要新增或替換圖片；XML 日期不會改變讀者畫面或內容理解。
- 問題與風險：無視覺風險；Google 何時重讀 sitemap 與視覺無關。
- 判定：`PASS`
- 修改指示與重測條件：無；若範圍擴及 HTML、CSS 或圖片，必須新增實際桌機／手機複驗與插畫判定。

### 複驗

- 不適用；初審沒有候選缺陷或後續修改。

## 3. 網站架構與互動

### 初審

- 驗收角色：前端維護 AI／品質檢查 AI
- 檢查版本：working tree R0
- 結構、連結、CTA、鍵盤與核心頁回歸證據：
  - `xmllint --noout sitemap.xml` 通過。
  - sitemap 為 34 個 `<loc>`、34 個唯一 URL、0 個草稿 URL；34/34 均對應本地檔案，canonical 與 URL 相符，沒有 `noindex`。
  - 本地 HTTP：首頁、`articles.html`、`articles/workplace-05.html`、`series/workplace.html`、`talks.html`、`sitemap.xml`、`robots.txt` 共 7/7 回 200。
  - 瀏覽器 DOM 回歸確認五個核心頁各有原有 H1：首頁「理解你的感受 陪伴你找到力量」、專欄入口、目標文章、職場系列與講座邀約。
  - 導覽、連結、CTA、鍵盤行為沒有檔案差異；不會因 XML 日期改變互動。
- 問題與風險：靜態檢查腳本初跑有驗證工具錯誤，已依上方備註更正並完整重跑；沒有候選架構缺陷。
- 判定：`PASS`
- 修改指示與重測條件：無；若 sitemap URL 數、順序或任一 HTML 變動，必須重新執行全站連結與互動測試。

### 複驗

- 不適用；初審沒有候選缺陷或後續修改。

## 4. SEO 與索引邊界

### 初審

- 驗收角色：SEO／發布維護 AI／搜尋成效與索引驗收 AI／品質檢查 AI
- 檢查版本：working tree R0
- 搜尋意圖、metadata、內部連結、canonical、robots、sitemap、JSON-LD 與草稿隔離證據：
  - 目標 URL 在 sitemap 只有 1 筆，且相鄰 `<lastmod>` 精確為 `2026-08-13`；舊日期配對為 0 筆。
  - `git diff --numstat -- sitemap.xml` 為 `1 1 sitemap.xml`；完整 diff 證明只有單一日期替換。
  - 其餘 33 個 URL 及日期不變；sitemap 仍為有效 XML，沒有 `drafts/` 或 `docs/drafts/`。
  - `robots.txt` 仍有且只有既有正式宣告 `Sitemap: https://yuchienpsy.com/sitemap.xml`。
  - 34/34 sitemap URL 為 indexable、self-canonical；metadata、內部連結、JSON-LD 與草稿 robots 全部零變更。
  - Search Console 既有 sitemap 已成功並探索 34 頁；目標頁已在 Google 服務中，所以本案不提交重複 sitemap、不做 Live Test、不重複 Request indexing。
- 問題與風險：準確 `lastmod` 仍只是一項提示，不能保證 Google 立即重抓、採用新版摘要、建立索引、排名或流量提升。
- 判定：`PASS`
- 修改指示與重測條件：無；發布後只驗證正式 sitemap 的日期與 Search Console 讀取／最後檢索狀態，不消耗重複索引額度。

### 複驗

- 不適用；初審沒有候選缺陷或後續修改。

## 5. 組織合作與講座邀約視角

### 初審

- 驗收角色：組織合作與講座邀約視角驗收 AI
- 檢查版本：working tree R0
- 企業主管視角：公開內容零變更，原有個人心理安全、團隊影響與組織程序的平衡不受影響；沒有新增對主管的預設或歸責。
- 人資／人才發展／員工關係視角：文章與講座合作路徑零變更；沒有把 HR 描述為天然中立、萬能或必然偏袒，也沒有新增制度或法律定論。
- 公部門承辦科員視角：可轉呈的標題、內容、來源、專業界線與合作入口不變；XML 日期不會造成公開語意或採購資訊誤解。
- 個人與團隊影響是否兼顧：沿用 8 月 13 日已驗證版本；本案不修改任何相關句子。
- 中立性與權力不對等處理：不變；沒有淡化霸凌、個人感受或權力不對等，也沒有偏袒任一方。
- 內部轉呈所需資訊是否充分：不變；本案沒有新增或移除資訊。
- 講座邀約信任與阻礙：沒有新的阻礙；也不把技術 SEO 維護包裝成內容或合作成效。
- 問題、證據與風險：唯一風險是誤把 sitemap 日期校正宣稱為內容更新或排名成果；已在總管回報與 SEO 關明確禁止。
- 判定：`PASS`
- 修改指示與重測條件：無；若日後改動公開職場文案，必須重新分別取得三種視角的實質回饋。

### 複驗

- 不適用；初審沒有候選缺陷或後續修改。

## 總管彙整

- 五關初審是否都有證據：是；每關均記錄版本、觀察、證據、風險、判定與重測條件。
- 所有 FAIL 是否都有修改紀錄：候選沒有 FAIL；驗證工具／環境失敗已保留並說明更正方式，沒有把它誤列為候選缺陷。
- 所有修改是否都有獨立複驗：R0 後沒有追加候選修改，因此無複驗輪次。
- 明確保持不變的內容：全部 HTML、CSS、JavaScript、圖片、公開文案、metadata、JSON-LD、canonical、robots、內部連結、CTA、其他 sitemap URL 與日期。
- 未驗證的外部狀態：尚未 commit、push、建立 PR、合併或發布；正式 sitemap 仍是舊日期；Google 重新讀取、重抓與搜尋成效均待發布後觀察。
- 整體判定：`PASS — READY FOR USER RELEASE APPROVAL`
- 使用者預覽重點：本地 sitemap 的目標 URL 日期為 2026-08-13；目標文章畫面與文字應完全沒有變化。
- 發布閘門：使用者已於 2026-08-16 再次明確回覆「核准上線」；可 commit、push、建立 PR／合併與正式站驗證，但不得擴大檔案範圍。
