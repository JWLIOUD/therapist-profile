# 職場心理健康指南：Google 搜尋發現性五重驗收

任務 ID：`SEO-CONTENT-20260730-07`

日期／時區：2026-07-30／Asia/Taipei

候選版本：`codex/workplace-guide-nav`，HEAD `9a7d6be` 加未提交差異

狀態：`approved`

## 目標與不可改變事項

目標是讓 Google 能透過全站導覽、sitemap、canonical、結構化資料與圖片預覽訊號發現並理解職場心理健康指南。

不可改變事項：

- 不改指南、文章、講座、首頁或系列頁正文的表達原意。
- 不加入 `meta keywords`、隱藏文字或機械式關鍵字堆砌。
- 草稿維持 `noindex, nofollow`，不得加入 sitemap。
- 不保證 Google 收錄、排名、Discover 推播、曝光或流量。
- 未經使用者明確核准，不 commit、push、合併或部署。

## V1：初始檢查

### 已具備

- sitemap 已有且只有一筆 `https://yuchienpsy.com/workplace-mental-health.html`。
- `robots.txt` 已宣告正式 sitemap。
- 指南已有 `index, follow`、唯一 canonical、WebPage、BreadcrumbList 與七篇導讀 ItemList。
- 全站 34 個正式頁已有桌機及手機的標準 `<a href>` 指南入口。
- 首頁及文章列表另有具上下文的內容型入口。
- 指南已有 1600 × 900、16:9 專屬插畫。

### 可改善處

- 本輪實際改了 34 個正式頁的頁首連結，sitemap 的 `lastmod` 尚未同步反映這次重要連結更新。
- 圖片符合大型預覽尺寸，但指南尚未明確允許 `max-image-preview:large`。

### V1 判定

- 本輪需求不應重複新增 sitemap URL。
- 以日期同步及大型圖片預覽權限做最小 SEO 補強；不改正文或塞入新關鍵字。

## R1：最小修正

- `sitemap.xml` 的 34 個正式 URL 均更新為 `<lastmod>2026-07-30</lastmod>`。
- `workplace-mental-health.html` 的 robots meta 改為 `index, follow, max-image-preview:large`。
- title、description、H1、OG 文案、正文、canonical 與 JSON-LD 語意保持不變。

## V2：五重驗收

### 第 1 關：文案與語意保真

結果：PASS

- 本輪沒有改寫任何正式頁正文。
- 指南標題、摘要、H1 與「職場心理健康、壓力、霸凌、倦怠、求助方向」主題一致。
- 「職場心理健康」出現位置分布於標題、導覽、圖片替代說明、自然正文及結構化資料；沒有無關段落填塞。
- 未新增 Google 不使用的 `meta keywords`。
- 沒有療效、排名、收錄或流量保證。

### 第 2 關：視覺風格與無障礙

結果：PASS

- JPG 及桌機 WebP 實檔均為 1600 × 900、16:9。
- 插畫以溫和工作情境呈現壓力、界線、支持與休息，與頁面主題直接相關。
- 圖片沒有口號、Logo、大量文字、衝突或受害者化畫面。
- OG／Twitter 使用正式絕對 JPG URL，尺寸資料與替代說明一致。
- `<picture>` 保留手機 900 × 900 source、桌機 1600 × 900 fallback、實際檔案、alt 及 width／height。
- 本輪只改 head 內 robots 與 sitemap，不改可見版面。

非阻擋風險：Google 可能依卡片版位裁切圖片；極端裁切可能減少左側情境節點，但主體仍可辨識。

### 第 3 關：網站架構與互動

結果：PASS

- 34/34 正式頁都有桌機 dropdown 指南入口。
- 34/34 正式頁都有手機選單指南子項。
- 連結皆為標準 `<a href>`，根層及次目錄相對路徑正確，不依賴 JS 跳轉。
- 指南本地實頁載入完成，H1、桌機入口、手機入口均存在。
- 1265px 實頁檢查：`scrollWidth` 與 `clientWidth` 同為 1265，沒有水平溢位。

### 第 4 關：SEO 與索引邊界

結果：PASS

- `xmllint --noout sitemap.xml` 通過。
- sitemap 有 34 個 `<url>`、34 個唯一 `<loc>`；指南恰好一筆。
- 34 個 `lastmod` 均為 `2026-07-30`，且每個正式 URL 都能對應 repo 檔案。
- sitemap 不含 `drafts/` 或 `docs/drafts/`。
- 發布前完整掃描第一輪 FAIL：原本只檢查 `drafts/` 的 5 個 HTML，擴大到 `docs/drafts/` 後發現擱置的職場霸凌委員草稿仍為 `index, follow`。
- R2：只將 `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html` 改為 `noindex, nofollow`，草稿正文與正式頁均未改。
- R2 複驗：`drafts/` 與 `docs/drafts/` 共 6 個草稿 HTML 全部為 `noindex, nofollow`，且 sitemap 草稿 URL 仍為零。
- 指南 robots 為 `index, follow, max-image-preview:large`。
- canonical 為 `https://yuchienpsy.com/workplace-mental-health.html`。
- OG image 為 1600 × 900 正式 HTTPS URL。
- WebPage、BreadcrumbList 及七篇文章 ItemList 結構化資訊保留。
- `git diff --check` 通過。

正確對外表述：

> 目前頁面具備 Google Discover 的技術候選條件，但不保證被選入、推播、取得曝光或流量。

### 第 5 關：組織合作與講座邀約視角

結果：PASS

- 企業主管：標題雖提及霸凌，但與壓力、倦怠及求助並列，沒有指控特定主管或企業。
- 人資／人才發展／員工關係：搜尋預覽同時涵蓋風險辨識、自我照顧與求助，未承諾診斷、調查結論、法律結果或療效。
- 公部門承辦：用語正式且沒有法律或行政定性；圖片平和，適合作為活動研究或講座候選資料。
- 指南既有「不診斷、不判定霸凌、不取代人事／申訴」界線保持不變。
- `max-image-preview:large` 只允許較大型圖片預覽，不代表 Google 一定顯示。

## V2 總結

- 五關均 PASS。
- 阻擋問題：無。
- 狀態：`user_preview`。
- 發布閘門：仍需使用者明確核准上線。

## V3：使用者核准後發布前掃描

- 使用者於 2026-07-30 明確核准上線。
- 自動檢查器第一輪因假設桌機子連結具有額外 class 而誤判首頁缺漏；核對實際 `.nav-submenu` 結構後修正檢查條件，網站程式不需修改。
- 擴大草稿掃描範圍後發現 `docs/drafts/` 擱置稿的 robots 邊界問題，判定 SEO 發布前檢查 FAIL。
- 完成 R2 後重新執行 XML、URL 唯一性、34 頁桌機／手機導覽、全部草稿、canonical、OG 圖、JSON-LD、產生器語法與 diff 檢查。
- R2 複驗通過後才允許進入 commit／push／PR。

## 本地與發布後檢查

本地預覽：

- `http://127.0.0.1:8015/workplace-mental-health.html`

發布後才執行：

1. 確認正式指南、OG 圖與 sitemap 均為 HTTP `200`。
2. 確認正式 source 保留 robots、canonical、OG 尺寸及結構化資料。
3. 在 Search Console 查看 sitemap 與 URL Inspection 狀態。
4. 若 URL 已申請、處理中、已在 Google 服務中或已收錄，不重複 Request indexing。
5. 只記錄實際 Search／Discover 回饋，不把候選條件描述成保證成效。
