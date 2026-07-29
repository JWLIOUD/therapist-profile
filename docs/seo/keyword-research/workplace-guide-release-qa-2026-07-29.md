# 職場心理健康導航頁：正式發布前四重驗收

日期：2026-07-29
任務 ID：`SEO-CONTENT-20260725-03`
正式候選 URL：`https://yuchienpsy.com/workplace-mental-health.html`
使用者授權：已明確要求完成四重驗收並正式發布

## 總結

| 驗收環節 | 第一輪 | 修正 | 第二輪 |
| --- | --- | --- | --- |
| 文案 | PASS | 無 | PASS |
| 視覺風格 | FAIL | 手機改為 H1／導讀／CTA 優先；統一卡片連結色與提醒框色票 | PASS |
| 網站架構 | PASS | 無阻擋修正 | PASS |
| SEO | FAIL | 正式 robots、canonical、OG URL、JSON-LD URL、Breadcrumb、sitemap 與 lastmod | PASS |

四個環節均已通過；失敗項均完成退回修正與重測，沒有以第一次檢查結果直接放行。

## 1. 文案驗收

結論：PASS。

- 七篇導航摘要逐篇對照原文章，均忠於原文主張。
- 七篇既有文章沒有 diff；案例、心理觀點、結論、來源與作者歸屬未修改。
- 新頁只做總論與導讀，不搬入完整案例或完整解法。
- 明示不替讀者下診斷，也不判定事件是否構成職場霸凌。
- 沒有療效承諾、法律定論、恐嚇、標題黨或未確認服務。
- LINE 預約與講座合作沿用現站已公開服務；心理支持不取代醫療、法律、人事、申訴或緊急協助。

## 2. 視覺風格驗收

第一輪：FAIL。

- 手機版原本把方形插畫與閱讀提醒整組放在 H1 前，導致標題與主要 CTA 掉出首屏。

修正：

- 移除手機 `order: -1`，改為 H1、導讀與 CTA 優先，插畫與閱讀提醒其次。
- 卡片連結使用全站 `--sage-dark`。
- 閱讀提醒框使用全站 line 與 brown 陰影色。
- CSS cache key 更新為 `20260729-2`，避免瀏覽器沿用預覽版樣式。

第二輪：PASS。

- 桌機主圖 1600×900 WebP；手機使用獨立構圖的 900×900 WebP；社群預覽為 1600×900 JPG。
- 圖片沒有文字、Logo、醫療診斷符號、暴力、污名化情境或明顯生成瑕疵。
- 390×844 瀏覽器實測：H1 top 172px、bottom 294px；主圖 top 685px；無水平溢位。
- 手機載入 900×900 圖，桌機載入 1600×900 圖；無壞圖。
- 七張卡片桌機為前四張兩欄、後三張三欄；手機為單欄。

## 3. 網站架構驗收

結論：PASS。

- 新頁具有單一 H1 與七張文章導航卡。
- 首頁、心理專欄、職場系列頁各有一個語意清楚的 inbound link。
- 新頁導向七篇職場文章、完整職場系列、講座頁、服務與聯絡位置。
- 12 個核心頁 HTML 靜態檢查：H1、ID、JSON-LD、相對連結與資源路徑均無錯誤。
- 首頁、心理專欄、職場系列、新頁、七篇文章、講座頁、新 CSS 與三個插畫資產本地 HTTP 均為 `200`。
- 桌機核心頁無水平溢位；新頁桌機與手機瀏覽器 console 無 warning／error。
- 擱置草案及既有 SEO 測試文沒有加入正式導覽或 sitemap。

## 4. SEO 驗收

第一輪：FAIL。

- 新頁仍為 `noindex, nofollow`，缺 canonical、`og:url`、WebPage URL、Breadcrumb 最末 URL 與 sitemap。

修正：

- robots 改為 `index, follow`。
- canonical、`og:url`、WebPage `url` 與 Breadcrumb item 全部統一為正式 URL。
- WebPage 加入 `@id` 與 `primaryImageOfPage`。
- sitemap 新頁只出現一次，lastmod 為 2026-07-29。
- 首頁、文章列表、職場系列頁因新增入口，同步更新 lastmod；七篇未改文章維持原日期。
- sitemap 不包含 `drafts/` 或 `docs/`。

第二輪：PASS。

- 兩段 JSON-LD 均可解析；sitemap 通過 `xmllint --noout`。
- title、description、H1、可見內容、OG 與結構化資料搜尋意圖一致。
- 新頁為「職場心理健康」總論分流；系列頁、霸凌、倦怠、同情疲勞與講座頁維持獨立意圖，互搶風險可控。
- 不使用 Article 或 FAQPage 追求不適用的 rich result。

## 發布後必要驗證

- 正式新頁、CSS 與三個圖片資產回應 `200`。
- 正式 HTML 顯示 `index, follow`、self-canonical、`og:url` 與可解析 JSON-LD。
- 正式 sitemap 含新頁一次，且不含草稿。
- 首頁、文章列表與職場系列頁的入口可用。
- Search Console 先讀取 URL 狀態；若已送出、已在 Google 服務中或已編入索引，不重複 Request indexing。
- 以 7／28／90 天 query、page、click、impression、CTR 與 average position 回饋趨勢及 SEO 文案團隊。

## 非阻擋後續

- 七篇既有文章的 meta description 多為故事開頭，可另開只修改 metadata 的小型 SEO 需求；不得在本次發布擴張範圍。
- 若要讓七篇文章反向連回導航頁，需另做共用文末區塊與全文章版型回歸。

## 正式發布與線上驗收

- PR：`https://github.com/JWLIOUD/therapist-profile/pull/1`
- PR 狀態：`MERGED`
- 正式 main commit：`9c3b35b97508b827f4245ff5c4f6b950381d41c5`
- GitHub Pages build：`built`
- 正式新頁、CSS、桌機 WebP、手機 WebP、社群 JPG、首頁、文章列表與職場系列頁：全部 HTTP `200`。
- 線上新頁：單一 H1、七張導航卡、`index, follow`、self-canonical、`og:url` 與兩段可解析 JSON-LD 均通過。
- 線上 sitemap：正式 URL 出現一次，沒有 `drafts/` 或 `docs/`。
- 正式桌機：1600×900 WebP 載入完成，無壞圖、無水平溢位、console 無 warning／error。
- 正式 390×844 手機：900×900 WebP 載入完成，H1 top 172px／bottom 294px，主圖 top 685px，七張卡均為單欄，無水平溢位、console 無 warning／error。
- 三個正式 inbound：
  - 首頁：「先看職場心理健康指南」
  - 心理專欄：「依照職場困擾找文章」
  - 職場系列：「先看職場心理健康指南」

網站端結論：`verified`。Google 是否收錄與後續成效仍需依 Search Console 7／28／90 天流程觀察，不把網站發布完成等同 Google 已收錄。
