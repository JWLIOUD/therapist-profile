# 網站總管作業制度

更新日期：2026-07-25

## 目的

這份文件是黃郁倩諮商心理師網站的 AI 維護入口。所有 AI 角色在工作前必須先讀：

1. `AGENTS.md`
2. `docs/maintenance-workflow.md`
3. `docs/ai-team/ai-roles.md`
4. 本次任務對應的 `docs/workflows/*.md`
5. `docs/todos/latest-todos.md`
6. `docs/ai-team/handoffs.md` 的最新相關紀錄

若文件與使用者最新明確決定衝突，以使用者最新決定為準，並由網站總管更新文件。

## 專案與發布邊界

- 靜態 GitHub Pages 網站，正式網域為 `https://yuchienpsy.com/`。
- 核心頁：`index.html`、`articles.html`、`talks.html`。
- 文章：`articles/*.html`；系列頁：`series/*.html`。
- 全站樣式：`styles.css`、`articles.css`、`article.css`、`series.css`。
- SEO：`sitemap.xml`、`robots.txt`、各頁 canonical、metadata 與 structured data。
- 正式發布分支為 `main`；未經使用者明確同意不得直接推送 `main`。
- 研究報告、交接文件與內部草稿不加入公開導覽或 sitemap。
- `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html` 為擱置素材，不得正式化。
- `drafts/workplace-mental-health-seo-test.html` 必須維持 `noindex, nofollow`，不得加入文章列表、系列頁、sitemap 或 Search Console。

## 統一任務生命週期

每項工作都必須依序經過以下狀態：

1. `intake`：總管接收需求並確認目的。
2. `scoped`：完成範圍、限制、風險與負責角色。
3. `assigned`：總管建立需求單並派工。
4. `in_progress`：執行角色只處理核准範圍。
5. `review`：SEO、內容、前端或品質角色依任務進行獨立檢查。
6. `user_preview`：需要內容、視覺、服務或發布決策時交使用者預覽。
7. `approved`：使用者核准可發布範圍。
8. `published`：完成 commit、push 與部署；只有使用者授權才可進入。
9. `verified`：正式站與 Search Console／SERP 的適用驗收完成。
10. `closed`：交接、待辦、驗證與剩餘風險均已記錄。

未完成前一個必要閘門，不得宣稱後一狀態已完成。

## 網站總管需求單

任何會修改檔案的任務，總管必須先建立需求單。最低欄位：

- 任務 ID、名稱、建立日期與來源。
- 目標與成功標準。
- 目標頁面／檔案。
- 在範圍內與不在範圍內。
- 使用者已確認的事實與仍需決定事項。
- 不可改變的內容、語意或品牌界線。
- 負責角色、審查角色與交接順序。
- 每個角色的具體交付物。
- 本地驗證、使用者預覽與發布條件。
- 風險、回復方式與成效追蹤指標。

需求不完整但可安全推進時，總管以明確假設處理；若假設會改變服務、專業主張、法律／醫療內容、對外發布或使用者決策，必須先停下確認。

## 統一交接閘門

每次角色交接必須包含：

- 任務 ID 與目前狀態。
- 交接來源與接手角色。
- 已完成事項與實際修改檔案。
- 明確未完成事項。
- 證據、測試、預覽網址或報告連結。
- 不可改變的決策與已知風險。
- 接手角色的下一步與完成條件。
- 是否需要使用者決定。

「已分析」、「已修改」、「已驗證」、「已發布」是不同狀態，不得混用。沒有證據的項目標示「未驗證」。

## 核心品質原則

- 心理健康內容保持專業、溫和、清楚，不診斷、不保證療效。
- 法律、醫療、危機資源、資格、費用、服務地點與聯絡方式不得自行推測。
- 修改既有內容時保留原文核心意思、心理觀點、案例意義、專業主張、結論與來源。
- SEO 關鍵字必須自然；即時話題不能凌駕讀者助益與專業倫理。
- URL 改動同步檢查內部連結、canonical、sitemap 與 redirect 需求。
- 視覺改動同時驗證桌面與手機，並對照首頁、文章列表與相關系列的字體、色彩、圓角、留白、卡片及 CTA。
- 每個新增頁面都要由品牌素材 AI 判斷圖片是否足以支持內容與品牌風格；有相符核准素材時優先重用，缺少時才由插畫設計 AI 依 brief 產出候選。
- 插畫必須放回本地頁面後再驗收題意、裁切、alt、效能與心理健康呈現，不能只驗收單張圖。
- 每次只做可審查的小範圍改動，避免無關重構。
- 品質檢查角色不得直接替執行角色修改後自我核准；需要修正時退回負責角色。

## 工作流路由

| 任務類型 | 必讀工作流 |
|---|---|
| 心理健康搜尋趨勢與議題情報 | `keyword-trend-research.md` |
| 趨勢驅動的既有內容 SEO 更新 | `seo-trend-content-update.md` |
| Search Console 索引與流量成效回饋 | `search-performance-feedback.md` |
| 新增正式文章 | `new-article.md` |
| 修改服務、預約或 CTA | `update-service-info.md` |
| 更新講座紀錄與邀約頁 | `update-talk-records.md` |
| 任何準備發布的改動 | `pre-publish-check.md` |

一項任務可同時套用多條工作流；網站總管需在需求單中明列順序。

## Git 與發布規則

- 開始前確認分支、遠端與工作樹，保留使用者既有變更。
- 未經授權不切換或推送 `main`。
- commit 只包含同一需求單的相關檔案。
- commit 前必須執行 `pre-publish-check.md` 的適用項目。
- 發布後要記錄 commit、部署結果、正式站驗證與未完成的外部驗收。
- Google 尚未重新抓取不等於部署失敗；網站端完成與 Google SERP 完成分開記錄。
- Search Console 查看屬於唯讀驗收；提交 sitemap、要求建立索引或其他會改變外部狀態的操作，必須由使用者明確授權。
- 已要求建立索引、已在 Google 服務中或已編入索引的 URL，不得為了加速而重複送出申請。

## 本地預覽

從 repository 根目錄執行：

```bash
python3 -m http.server 8013 --bind 127.0.0.1
```

開啟：

```text
http://127.0.0.1:8013/
```

若環境限制本地監聽，取得使用者允許後再啟動；不可因無法開啟瀏覽器而省略可執行的靜態、連結與 metadata 檢查。

## 完成回報

總管結案時必須回報：

- 完成的目標與目前狀態。
- 修改檔案與對使用者可見的差異。
- 驗證方式與結果。
- 明確保持不變的內容。
- 未完成事項、風險與下一步。
- 是否 commit、push、部署；若沒有，必須明說。
