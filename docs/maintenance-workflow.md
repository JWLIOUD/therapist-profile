# 網站維護工作流

## 目前網站架構

這是一個 GitHub Pages 靜態網站，正式網域由 `CNAME` 指向 `yuchienpsy.com`。網站沒有 npm、Vite、Next.js 或後端服務，主要由 HTML、CSS、圖片素材和少量 Python 產生工具構成。

主要區塊：

- 首頁：`index.html`
- 文章列表：`articles.html`
- 講座邀約頁：`talks.html`
- 文章頁：`articles/*.html`
- 專題系列頁：`series/*.html`
- 全站樣式：`styles.css`、`articles.css`、`article.css`、`series.css`
- 圖片與 QR code：`assets/`
- 文章產生工具：`tools/generate_articles.py`

## 網站總管 AI 的責任

網站總管 AI 不只是改檔案，應該負責維護「內容、技術、SEO、風險」的一致性。

固定責任：

- 檢查網站架構與檔案關聯後再修改。
- 控制每次改動範圍，避免一次改太多。
- 修改文案時保留心理健康內容的專業語氣。
- 修改文章或頁面路徑時同步檢查內部連結、canonical、sitemap。
- 修改版面後檢查手機與桌面顯示。
- 變更完成後回報改了什麼、如何驗證、下一步建議。

## 建議維護團隊

### 1. 網站總管 / 產品負責人

決定網站優先順序、內容發布節奏、服務資訊是否要調整。這個角色可以由你擔任，AI 協助整理需求與拆任務。

### 2. 內容編輯

負責心理健康文章、首頁文案、服務說明、CTA 文字。重點是保持專業、溫和、清楚，避免過度承諾療效。

### 3. 前端維護

負責 HTML/CSS、手機版排版、圖片壓縮、連結狀態、跨頁一致性。此網站目前不需要大型前端框架。

### 4. SEO / 發布維護

負責 `sitemap.xml`、`robots.txt`、meta description、Open Graph、canonical、GitHub Pages 發布檢查。

### 5. 品牌與素材管理

負責頭像、插圖、QR code、LINE 連結、色彩與視覺一致性。

## 建議工作流

### 日常小修改

1. 從 `main` 更新本地專案。
2. 建立修改分支。
3. 修改 HTML/CSS 或圖片。
4. 本地開啟靜態伺服器檢查。
5. 確認 `git diff`。
6. commit 後推送 GitHub。
7. 檢查 GitHub Pages 是否正常發布。

### 新增文章

1. 決定文章分類與 slug。
2. 新增 `articles/{slug}.html`。
3. 更新 `articles.html` 文章列表。
4. 更新對應 `series/{category}.html`。
5. 更新 `sitemap.xml`。
6. 檢查文章頁 meta、OG image、canonical、來源註記。

### 修改服務或預約資訊

1. 先確認 LINE、聯絡方式、服務內容是否為最新版本。
2. 修改首頁或 `talks.html`。
3. 檢查所有 CTA 是否一致。
4. 手機版優先檢查按鈕與聯絡區塊。

## 目前需要注意的技術債

- `README.md` 幾乎沒有維護資訊，建議下一步補成完整專案說明。
- `tools/generate_articles.py` 依賴 repo 外部 Word 檔與資料夾，之後應明確整理來源檔位置與使用方式。
- 沒有自動化連結檢查或 HTML 驗證，後續可加輕量工具。
- 沒有 GitHub Actions 發布前檢查，後續可加入 sitemap/link check。

## 本地開發指令

```powershell
cd C:\Users\roy81\Documents\therapist-profile
python -m http.server 8000
```

這台電腦目前沒有全域 `python` 指令，可先使用既有虛擬環境：

```powershell
cd C:\Users\roy81\Documents\therapist-profile
C:\Users\roy81\Documents\stock-telegram-alert\.venv\Scripts\python.exe -m http.server 8000
```

開啟：

```text
http://localhost:8000/
```
