# 全站職場心理健康下拉入口：五重驗收迴圈

任務 ID：`SEO-CONTENT-20260729-06`
基準 commit：`9a7d6be`
目前狀態：`user_preview`
預覽：`http://127.0.0.1:8015/talks.html`

## 修改版本

| 版本 | 修改 | 驗收結果 |
|---|---|---|
| V1 | 在「心理專欄」與「講座邀約」間新增獨立頂層「職場心理健康」 | 文案／SEO 條件式通過；視覺 FAIL |
| V2 | 依使用者決策改為「心理專欄」hover／focus 下拉；手機改縮排子項 | 文案、SEO、組織視角 PASS；視覺條件式 FAIL |
| V3 | 完整桌機導覽斷點改為 1120px；手機選單加入可視高度、捲動與 visibility；裝飾箭頭改為 `aria-hidden` | 五關最終 PASS |
| V4 | 擴大到文章列表、25 篇文章、5 個系列與指南；同步四套正式 CSS 及產生器 | 文案／ARIA FAIL；架構與組織跨裝置 FAIL；SEO PASS |
| V5 | 修正 current 語意，補齊 34 頁手機導覽，共用 navigation CSS／JS，完成快取更新與跨裝置重測 | 五關 PASS，等待使用者預覽 |

## 1. 文案與語意保真

### V1 初審

- 「職場心理健康」與正式指南及首頁卡片語意一致，沒有療效或服務承諾。
- 風險：獨立頂層項可能被理解為另一種服務，且需等待視覺容納驗證。
- 判定：`CONDITIONAL PASS`。

### V2 複驗

- 「心理專欄 → 職場心理健康」更準確表達指南是專業內容，而不是另一種諮商或企業顧問服務。
- 保留父層「心理專欄」前往 `articles.html`；子項前往正式指南。
- 手機依序呈現「心理專欄、職場心理健康、講座邀約」。
- 未改首頁正文、指南、服務或個案內容。
- 判定：`PASS`。

## 2. 視覺風格與無障礙

### V1 初審

- 問題：新增第八個桌機頂層連結，在 900／1024px 有換行、碰撞與截字風險。
- 判定：`FAIL`。
- 修改：依使用者決策改為既有「心理專欄」的下拉子項。

### V2 複驗

- 通過：桌機頂層恢復七項；下拉沿用品牌色、圓角、陰影，支援 hover 與 `focus-within`。
- 問題：390 × 568 手機選單新增一項後高度超過可視區，而原選單沒有 `max-height` 或捲動。
- 判定：`FAIL`。
- 修改：
  - `max-height: calc(100dvh - var(--header-height))`
  - `overflow-y: auto`
  - `overscroll-behavior: contain`
  - 收合／展開加入 `visibility: hidden/visible`
  - 完整桌機導覽斷點由 900px 改為 1120px
  - 手機裝飾箭頭改用 `aria-hidden` span

### V3 複驗

- 900／1024px：使用 46 × 46px 漢堡選單，無水平溢位。
- 1120／1280px：完整導覽無品牌／導覽／CTA overlap，無水平溢位。
- 1240px 以上才增加導覽水平 padding。
- 390 × 568：選單 client height 493px、scroll height 589px，可捲至 LINE CTA；子項高度 56.8px。
- 收合選單 `visibility:hidden`、`pointer-events:none`；展開後可操作。
- `↳` 為 `aria-hidden`，連結可存取名稱為「職場心理健康」。
- 鍵盤聚焦「心理專欄」後，子選單 opacity 1、visibility visible，子項可 Tab 到達。
- 判定：`PASS`。
- 非阻擋增強：CSS-only 下拉未同步 `aria-expanded`，也未實作 Esc 關閉；目前使用一般 nav links，Tab／Shift+Tab 可正常離開。

## 3. 網站架構與互動

### 最終驗收

- 桌機頂層仍為七項；指南入口只在「心理專欄」子選單出現。
- 手機選單有一個縮排子項。
- 首頁共有三個指向正式指南的自然入口：桌機子選單、手機子項、內容卡片。
- 桌機鍵盤 `focus-within` 實際開啟子選單，子項唯一且可點。
- 手機 390 × 568 實際展開選單，子項唯一且可點。
- 兩種入口均進入 `workplace-mental-health.html`；H1 與 canonical 正確。
- `git diff --check` PASS。
- 判定：`PASS`。

## 4. SEO 與索引邊界

### V1 初審

- 標準 `<a href>`，沒有 JavaScript 導航或 nofollow。
- 判定：`CONDITIONAL PASS`，等待互動與部署回歸。

### V2 複驗

- 下拉 CSS 不移除 HTML href，搜尋引擎仍可解析。
- 「心理專欄 → 職場心理健康」階層符合內容分類。
- 首頁卡片保留較長 anchor，與短導覽 anchor 互補。
- 正式指南維持 `index, follow`、正確 canonical，sitemap 只有一筆正式 URL。
- 未修改 sitemap、metadata、JSON-LD 或草稿隔離。
- 判定：`PASS`。
- 上線後重測：首頁及指南 HTTP 200、正式 href、canonical、robots 與 sitemap。

## 5. 組織合作與講座邀約視角

### V1 初審

- 企業主管、人資及公部門承辦均認為「職場心理健康」是中性、可安全轉呈的名稱。
- 指南既有不診斷、不判定霸凌、不取代人事／申訴等界線未變。
- 判定：`PASS`。

### V2 複驗

- 企業主管：歸入專欄可避免被誤認為對主管／組織的指控或獨立顧問服務。
- 人資：形成「心理專欄 → 職場指南 → 講座合作」的內容評估路徑。
- 公部門承辦：清楚區隔知識文章、制度處理與講座合作。
- 頂層「講座邀約」維持不變，不用傷害性標題換取邀約。
- 指南正文、個人／團隊平衡與專業界線均未修改。
- 判定：`PASS`。
- 重測條件：若指南免責／制度文字、講座 CTA 或導覽層級改變，需重新驗收。

## V4 全站擴充初審

### 擴充範圍

- 根目錄：首頁、講座頁、文章列表、職場指南，共 4 頁。
- 文章內頁：`articles/*.html` 共 25 頁。
- 正式系列頁：`series/*.html` 共 5 頁；`series/addiction-01.html` 為 `noindex, follow` 相容轉址頁，不納入正式頁首。
- 總計 34 個正式頁首；`tools/generate_articles.py` 同步桌機導覽。

### 五關初審

- 文案與語意保真：`FAIL`。
  - `series/workplace.html` 曾錯把指南子項標示為目前頁。
  - 指南頁父層「心理專欄」與指南子項曾同時使用 `aria-current="page"`。
- 視覺風格與無障礙：桌機配置 `PASS`；trigger 與子項改為 `white-space: nowrap`、子選單最小寬度 168px。
- 網站架構與互動：`FAIL`；桌機 34/34 有 dropdown，但手機只有首頁與講座頁 2/34 有替代導覽。
- SEO 與索引邊界：`PASS`；新增的是標準 href，正式指南 canonical、robots、sitemap 與草稿隔離未變。
- 組織合作與講座邀約視角：`FAIL`；內容中立性通過，但組織窗口轉傳文章給手機讀者時，對方無法從頁首找到同一指南路徑。

### V4 判定

- 不得以首頁 V3 PASS 直接放行全站版本。
- 必須修正 current 語意，並補齊文章列表、文章、系列與指南的手機導覽後重測。

## V5 全站修正與複驗

### 修改

- 34/34 頁保留桌機「心理專欄 → 職場心理健康」下拉。
- 34/34 頁新增或保留 hamburger、`#mobileMenu` 與縮排 `.mobile-sub-link`。
- 新增 `navigation.css`：
  - 46 × 46px hamburger。
  - 短螢幕 `max-height`、垂直捲動與 overscroll 控制。
  - 子項 nowrap、縮排與 `aria-hidden` 裝飾箭頭。
  - 900px 精確切換文章列表、文章與系列的手機／桌機導覽。
- 新增 `navigation.js`：
  - 同步 `aria-expanded` 與按鈕標籤。
  - 點擊連結後收合。
  - Escape 關閉並復原焦點。
  - 跨斷點 resize 時清除開啟狀態。
- 指南沿用 `styles.css` 的 1120px 切換；正式根層樣式版本升為 `20260729-nav-dropdown-3`。
- 文章列表引用 `articles.css?v=20260729-nav-dropdown-2`；文章與系列共用樣式維持新的 `...nav-dropdown-1`。
- `tools/generate_articles.py` 同步桌機 dropdown、手機導覽、navigation CSS／JS 與 current 規則。
- 修正：
  - `series/workplace.html` 指南子項移除錯誤 current。
  - 指南頁父層「心理專欄」移除 current，只保留真正指南子項。
  - 每個正式頁最多一個 `aria-current="page"`。

### 實際瀏覽器與靜態證據

- 34 個正式頁：dropdown 34/34、hamburger 34/34、mobile menu 34/34、mobile sub-link 34/34。
- 900px 文章列表：完整導覽保留；品牌至導覽、導覽至 CTA 各約 20.5px；無水平溢位。
- 1024px 文章內頁：桌機導覽無碰撞；trigger／子項均 nowrap。
- 1120px 講座頁：桌機導覽無碰撞；鍵盤 focus 開啟子選單，動畫完成後 opacity 1、visibility visible。
- 390 × 568：
  - 講座頁既有手機選單可捲動；子項高度約 56.8px。
  - 文章內頁新選單可開啟；子項高度約 57.6px、nowrap、無水平溢位。
  - 文章列表、系列與指南的子項均可見且相對路徑正確。
  - 文章內頁 Escape 後 `aria-expanded=false`、visibility hidden、pointer-events none，焦點回到 hamburger。
- 從文章內頁手機子項實際進入指南；H1 與 canonical 正確。
- console 無 error／warning。
- 文章產生器語法 PASS，`page_header()` 靜態輸出檢查具備 dropdown、hamburger、mobile menu、mobile sub-link、指南 href，且 current 不重複。
- `git diff --check` PASS。

### 五關複驗

- 文案與語意保真：`PASS`；正文、H1、服務表達、meta description 與 JSON-LD 未改。
- 視覺風格與無障礙：`PASS`；390 × 568、900、1024、1120、1280 的代表頁型均無文字換行、重疊或水平溢位。
- 網站架構與互動：`PASS`；桌機與手機均為 34/34，根層與子目錄相對路徑均正確。
- SEO 與索引邊界：`PASS`；標準 crawlable href，canonical、robots、sitemap 與 drafts 邊界不變。
- 組織合作與講座邀約視角：`PASS`；企業主管、人資／人才發展／員工關係及公部門承辦的跨裝置轉傳路徑一致，沒有新增歸責或調查認定語意。

### 非阻擋技術債

- 25 篇文章與 5 個系列沿用既有 `aria-current="page"` 表示目前位於心理專欄區段；日後可另案改為 `aria-current="location"` 或 CSS class。
- 首頁／講座頁使用既有 inline mobile script，其餘頁型使用共用 `navigation.js`；目前實機通過，但長期可另案統一。
- 桌機 CSS-only dropdown 未動態同步 `aria-expanded`；hover、focus-within 與 Tab 路徑已可操作。
- 文章列表恰好 900px 的餘裕最小，未來不應再增加頂層項目或更長標籤而不重測斷點。

## 總管結論

- V1、V2、V4 的 FAIL 與修正均保留，沒有以最終 PASS 覆蓋。
- V5 已通過全站五重本地驗收。
- 未修改指南、文章、講座內容、索引設定或 sitemap。
- 目前不得 commit、push、合併或部署；等待使用者預覽並核准上線。
