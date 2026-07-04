# Google 搜尋結果 Logo 選項

更新日期：2026-07-05

## 背景

Google 搜尋結果目前仍顯示被縮小的人像照片，品牌感不足，且在小尺寸下容易顯得不正式。本輪先建立 3 個非照片、暖色系、與網站風格一致的 logo 選項，等使用者選定後再替換正式 favicon 與 `site-icon-512.png`。

## AI 團隊分工

- 網站總管 AI：整理需求、確定不直接替換正式站資產，先產出可選方案。
- 品牌素材 AI：設計 3 個非照片圖示，使用網站既有色彩 `cream / almond / peach / sage / brown`。
- SEO / 發布維護 AI：確認圖示適合做 Google 搜尋結果 favicon，需保留 512x512、192x192、48x48 與 `.ico` 版本的後續輸出流程。
- 前端維護 AI：本輪不改正式 `<link rel="icon">`，避免未經選定的設計直接上線。
- 品質檢查 AI：確認圖示為正方形，且預覽包含 48px 小尺寸效果。

## 選項

### A. 暖印章「郁」

- 檔案：`assets/logo-options/option-1-warm-seal-yu.png`
- 特色：以「郁」字做正式品牌識別，搭配暖色圓章與 sage 色環。
- 優點：小尺寸仍清楚，最容易和心理師本人姓名連結。
- 風險：較像個人印章，視覺上比圖案型 logo 更正式。

### B. 傾聽心形

- 檔案：`assets/logo-options/option-2-listening-heart.png`
- 特色：抽象心形與傾聽線條，不使用照片或文字。
- 優點：溫柔、有諮商感，和心理支持品牌氣質相符。
- 風險：與姓名連結較弱，需要搭配搜尋結果中的網站名稱一起建立識別。

### C. YP 字標

- 檔案：`assets/logo-options/option-3-calm-yp.png`
- 特色：使用 `YP` 字標與柔和色塊，對應 yuchienpsy。
- 優點：現代乾淨，較像正式網站或品牌縮寫。
- 風險：中文使用者不一定第一眼知道 `YP` 代表黃郁倩心理師。

## 預覽

- 總覽圖：`assets/logo-options/logo-options-preview.png`
- 總覽圖包含每個選項的 512px 主視覺與 48px 小尺寸預覽。

## 待使用者決策

- [x] 使用者選擇 A / B / C 其中一個：已選 A 暖印章「郁」。
- [ ] 使用者從 A 的字體版本中選擇 A1 / A2 / A3。
- [ ] 若需要，可依使用者意見微調顏色、字重、圖形比例。
- [ ] 選定後輸出正式 favicon 套件：
  - `favicon.ico`
  - `assets/favicon-48.png`
  - `assets/favicon-192.png`
  - `assets/apple-touch-icon.png`
  - `assets/site-icon-512.png`
- [ ] 替換後執行發布前檢查與 Google 實際搜尋結果截圖驗收。

## A 暖印章「郁」字體版本

使用者已選定 A 的方向，但希望字體更有活力。本輪保留暖印章外框，僅調整「郁」字字體氣質。

### A1. 活潑明體

- 檔案：`assets/logo-options/option-a1-lively-serif-yu.png`
- 特色：保留正式識別感，字形比原版更有動勢。
- 適合：想要穩重但不要太呆板。

### A2. 圓潤黑體

- 檔案：`assets/logo-options/option-a2-rounded-sans-yu.png`
- 特色：筆畫較厚，親切穩定，48px 小尺寸最厚實。
- 適合：優先考慮 Google 搜尋結果小圖清楚度。

### A3. 書寫楷體

- 檔案：`assets/logo-options/option-a3-kai-yu.png`
- 特色：較有人味與手寫感，是三版中最活潑。
- 適合：想要更柔軟、有個人溫度的識別。

### A 字體版本預覽

- 總覽圖：`assets/logo-options/option-a-font-variants-preview.png`
