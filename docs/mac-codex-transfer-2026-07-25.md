# Mac mini / MacBook Codex 接手交接

接手專案：黃郁倩諮商心理師網站

Repo：

```bash
git@github.com:JWLIOUD/therapist-profile.git
```

正式網站：

```text
https://yuchienpsy.com/
```

## 目前狀態

正式站最新已上線成果：

- 暖印章「郁」favicon / site icon 已正式採用並推上線。
- 最新正式 commit：`ea7bfa4 Record warm seal favicon deployment`
- 正式站目前不應包含「職場霸凌委員」獨立頁入口。

目前 Windows 桌電本機還有未提交草稿：

- `docs/ai-team/handoffs.md`
- `docs/meetings/meeting-notes.md`
- `docs/todos/latest-todos.md`
- `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html`
- `drafts/workplace-mental-health-seo-test.html`

重要：上述草稿尚未 commit、尚未 push、尚未上線。Mac 端若要完整接手，最好先請 Windows 端建立 WIP 分支並 push。

## 建議的無痛轉移方式

請先在 Windows 桌電 Codex 執行：

```bash
cd C:/Users/roy81/Documents/Codex/therapist-profile
git checkout -b codex/seo-workplace-drafts
git add docs/ai-team/handoffs.md docs/meetings/meeting-notes.md docs/todos/latest-todos.md docs/drafts drafts
git commit -m "Add workplace SEO drafts handoff"
git push -u origin codex/seo-workplace-drafts
```

如果 Windows 端已經完成 push，Mac mini / MacBook Codex 接手時執行：

```bash
git clone git@github.com:JWLIOUD/therapist-profile.git
cd therapist-profile
git fetch origin
git checkout codex/seo-workplace-drafts
git pull origin codex/seo-workplace-drafts
git status --short --branch
```

如果 Mac 已經 clone 過 repo：

```bash
cd therapist-profile
git fetch origin
git checkout codex/seo-workplace-drafts
git pull origin codex/seo-workplace-drafts
git status --short --branch
```

## 草稿說明

### 1. 擱置草案

```text
docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html
```

這是「職場霸凌調查委員／外聘心理師」獨立頁草案。

目前使用者決定：

- 暫時擱置。
- 不加入正式網站。
- 不加入首頁導覽。
- 不加入 `talks.html`。
- 不加入 `sitemap.xml`。
- 不提交 Search Console。

### 2. 內部 SEO 測試文

```text
drafts/workplace-mental-health-seo-test.html
```

這是「職場心理健康 × 職場霸凌 × 社會制度」SEO 改寫測試文。

目前設定：

- `noindex, nofollow`
- 不加入正式文章列表。
- 不加入系列頁。
- 不加入 sitemap。
- 僅供使用者預覽文案方向。

測試文鎖定關鍵字：

- `職場心理健康`
- `職場霸凌處理機制`
- `心理諮商如何幫助職場人`
- `職場倦怠預防`
- `心理健康與工作生活平衡`
- `職場性別平等與心理健康`
- `職場霸凌案例分享`

## 接手後第一步

請先確認目前分支與檔案：

```bash
git status --short --branch
ls docs/drafts
ls drafts
```

確認這兩個檔案存在：

```bash
test -f docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html && echo "shelved page exists"
test -f drafts/workplace-mental-health-seo-test.html && echo "seo test page exists"
```

## 本地預覽

這是純靜態網站，可以用任一簡單 server 預覽。

Mac 可用：

```bash
python3 -m http.server 8013
```

然後開：

```text
http://127.0.0.1:8013/drafts/workplace-mental-health-seo-test.html
```

也可以開原文章比較：

```text
http://127.0.0.1:8013/articles/workplace-05.html
```

## 驗收檢查

接手後請檢查：

```bash
grep -R "workplace-bullying-committee.html" index.html talks.html sitemap.xml || true
grep -R "workplace-mental-health-seo-test.html" index.html articles.html sitemap.xml series || true
grep -n "noindex, nofollow" drafts/workplace-mental-health-seo-test.html
```

預期：

- `index.html`、`talks.html`、`sitemap.xml` 不應出現 `workplace-bullying-committee.html`。
- `index.html`、`articles.html`、`sitemap.xml`、`series/` 不應出現 `workplace-mental-health-seo-test.html`。
- 測試文必須保留 `noindex, nofollow`。

## 下一步任務

請先請使用者確認測試文方向。

如果使用者喜歡目前 SEO 改寫方向，再討論三種正式化方式：

1. 直接改寫原文章：

```text
articles/workplace-05.html
```

2. 新增正式文章，例如：

```text
articles/workplace-mental-health.html
```

3. 規劃一組「職場心理健康」SEO 文章群，例如：

```text
職場心理健康總論
職場霸凌處理機制
職場倦怠預防
工作生活平衡
職場性別平等與心理健康
```

## 禁止事項

除非使用者明確同意，請不要：

- 把 `docs/drafts/workplace-bullying-committee-shelved-2026-07-07.html` 放進正式網站。
- 把 `drafts/workplace-mental-health-seo-test.html` 放進正式文章列表。
- 把草稿頁加入 `sitemap.xml`。
- 對草稿頁執行 Google Search Console URL Inspection 或 Request indexing。
- 直接 push 到 `main`。

## 工作流提醒

正式發布前一定要執行：

- 檢查首頁可開啟。
- 檢查 `articles.html` 可開啟。
- 檢查至少一篇文章頁可開啟。
- 檢查至少一個系列頁可開啟。
- 檢查 `talks.html` 可開啟。
- 檢查 sitemap URL 都存在。
- 檢查 robots。
- 檢查主要 CTA。
- 檢查 Email / Gmail CTA 不只是 `mailto:`，應能開 Gmail 或至少複製 Email 並顯示提示。
- 檢查所有內部連結是否 200 且有內容。

## 補充

Windows 桌電環境曾遇到：

- `Start-Process` 被權限擋。
- `python` / `py` 不可靠。
- `Invoke-WebRequest ... | Select-Object StatusCode,Content` 曾造成卡住。

請避免在 Windows 端輸出完整 sitemap 或整頁 HTML content。若要檢查正式站，只取 status code、content length、title、canonical、robots 等必要欄位，並設定 timeout。
