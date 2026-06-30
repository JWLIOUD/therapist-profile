# 固定流程：新增文章

負責角色：網站總管 AI、內容編輯 AI、SEO / 發布維護 AI、前端維護 AI、品質檢查 AI

## 觸發條件

你提供新文章、文章草稿、Word 來源、或要求新增某篇文章時啟動。

## 流程

1. 網站總管 AI 確認文章目標、分類、標題、slug、來源與是否要立即發布。
2. 內容編輯 AI 檢查標題、摘要、段落、語氣與專業風險。
3. 前端維護 AI 建立或更新：
   - `articles/{slug}.html`
   - `articles.html`
   - 對應 `series/{category}.html`
4. SEO / 發布維護 AI 檢查：
   - `<title>`
   - meta description
   - `robots` 是否為 `index, follow`
   - canonical
   - Open Graph
   - Article JSON-LD
   - `sitemap.xml`
5. 品質檢查 AI 執行發布前檢查。
6. 網站總管 AI 回報改動、驗證結果、剩餘風險。

## 必填資料

- 文章標題
- 文章分類
- 文章正文
- URL slug
- 是否有原刊來源
- 是否需要封面圖或沿用分類圖

## 完成標準

- 新文章可從 `articles.html` 點到。
- 新文章可從對應系列頁點到。
- 新文章 URL 已加入 `sitemap.xml`。
- 新文章頁有 canonical、meta description、OG、JSON-LD。
- 本機預覽沒有破版。
