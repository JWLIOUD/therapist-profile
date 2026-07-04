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
- [ ] 使用者從 A 的墨水手寫字版本中選擇 A7 / A8 / A9。
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

## A 暖印章「郁」飄逸可愛置中版

使用者回饋 A1-A3 的字體仍不夠飄逸可愛，且文字偏上會讓人煩躁。本輪保留 A 暖印章外框，將「郁」字移到視覺中心，並改成更柔軟、可愛、輕盈的字體方向。

後續使用者補充參考圖後，確認目標更接近活動常見的墨水手寫字，因此 A4-A6 視為上一輪過渡稿，不作為目前優先候選。

### A4. 飄逸楷體

- 檔案：`assets/logo-options/option-a4-floating-kai-centered.png`
- 特色：字形最柔軟，帶手寫感，視覺重心置中。
- 適合：想要溫柔、飄逸、比較有人味的版本。

### A5. 柔和明體

- 檔案：`assets/logo-options/option-a5-soft-serif-centered.png`
- 特色：比 A1 更輕盈，仍保留正式感與辨識度。
- 適合：想要在正式可信與飄逸感之間取得平衡。

### A6. 可愛圓體

- 檔案：`assets/logo-options/option-a6-cute-rounded-centered.png`
- 特色：筆畫最厚實，最親切，小尺寸清楚。
- 適合：優先考慮 Google 搜尋結果小圖的穩定可讀性。

### A 飄逸可愛置中版預覽

- 總覽圖：`assets/logo-options/option-a-centered-cute-variants-preview.png`

## A 暖印章「郁」墨水手寫字版

使用者補充參考圖後，明確希望是活動常見的墨水手寫字體。此輪改用手繪筆畫方式建立「郁」字，不再套用一般電腦字型；重點是筆畫有速度、帶手寫感、視覺重心置中，同時保留搜尋結果小圖的辨識度。

### A7. 清楚墨水字

- 檔案：`assets/logo-options/option-a7-ink-marker-clear.png`
- 特色：最接近活動手寫字，筆畫清楚，重心置中。
- 適合：想要手寫感，但仍希望 Google 小圖最穩定。

### A8. 可愛麥克筆

- 檔案：`assets/logo-options/option-a8-ink-marker-cute.png`
- 特色：筆畫更圓、更俏皮，中心穩定。
- 適合：想要可愛感更明顯。

### A9. 飄逸手寫字

- 檔案：`assets/logo-options/option-a9-ink-marker-flowing.png`
- 特色：筆畫更輕盈飄逸，但仍保留辨識度。
- 適合：想要更接近輕快手寫活動字。

### A 墨水手寫字版預覽

- 總覽圖：`assets/logo-options/option-a-ink-handwriting-preview.png`
