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

- [x] 使用者選擇 A / B / C 其中一個：曾選 A 暖印章「郁」，後續改為狗線條標示方向。
- [ ] 使用者從網路參考簡單線條狗版本中選擇 E1 / E2 / E3。
- [ ] 若需要，可依使用者意見微調顏色、字重、圖形比例。
- [ ] 選定後輸出正式 favicon 套件：
  - `favicon.ico`
  - `assets/favicon-48.png`
  - `assets/favicon-192.png`
  - `assets/apple-touch-icon.png`
  - `assets/site-icon-512.png`
- [ ] 替換後執行發布前檢查與 Google 實際搜尋結果截圖驗收。

## D 狗線條標示

使用者將方向改為「一隻用簡單線條構成的狗」作為主體。此方向不再使用文字或人像，目標是在 Google 搜尋結果小圖中呈現溫暖、陪伴感與正式品牌感。

使用者後續要求直接上網查「簡單線條狗」並用相關圖片作為模仿目標，因此 D1-D3 視為未採用草稿；目前優先候選改為 E1-E3。

### D1. 環抱線條狗

- 檔案：`assets/logo-options/option-d1-curled-line-dog.png`
- 特色：圓形姿態像被安放、陪伴與保護。
- 適合：想要最溫暖、最貼近心理支持感的版本。

### D2. 坐姿線條狗

- 檔案：`assets/logo-options/option-d2-sitting-line-dog.png`
- 特色：輪廓最清楚，48px 小尺寸辨識度最好。
- 適合：優先考慮 Google 搜尋結果小圖穩定清楚。

### D3. 暖心線條狗

- 檔案：`assets/logo-options/option-d3-heart-line-dog.png`
- 特色：加入小暖心符號，情感記憶點較強。
- 適合：想要比較可愛、有溫度、但仍維持簡潔的版本。

### D 狗線條標示預覽

- 總覽圖：`assets/logo-options/option-d-line-dog-preview.png`

## E 網路參考簡單線條狗

本輪先搜尋「簡單線條狗 / simple line dog logo / minimal line dog icon」等相關圖片，整理常見風格方向後重新設計原創候選。參考重點是「圓框狗頭」、「坐姿一筆線狗」、「站姿幾何狗」三種常見類型，不照抄單一圖片。

### 參考方向

- 圓形狗頭 logo：圓框、側臉狗頭、線條穩定，適合正式標示。
- 坐姿 one-line dog：單線坐姿、尾巴與身體連成流動線條，較溫柔親近。
- 站姿幾何線條 dog：輪廓俐落、幾何感強，小尺寸辨識度高。

### E1. 圓框狗頭

- 檔案：`assets/logo-options/option-e1-circle-dog-head.png`
- 特色：參考圓形狗頭 logo 類型，最正式穩定。
- 適合：想要 Google 搜尋結果看起來像正式網站品牌。

### E2. 坐姿一筆線狗

- 檔案：`assets/logo-options/option-e2-one-line-sitting-dog.png`
- 特色：參考 one-line dog 類型，最溫柔親近。
- 適合：想要陪伴感、心理支持感比較明顯。

### E3. 站姿幾何狗

- 檔案：`assets/logo-options/option-e3-geometric-standing-dog.png`
- 特色：參考站姿線條 icon 類型，小尺寸最俐落。
- 適合：優先考慮搜尋結果 favicon 的辨識度。

### E 網路參考線條狗預覽

- 總覽圖：`assets/logo-options/option-e-web-line-dog-preview.png`

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

後續使用者再補充更多活動手寫字參考，確認方向是「講義、活動筆記、麥克筆墨水」的字感。A7-A9 是初步手繪稿，目前優先候選改為 A10-A12。

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

## A 暖印章「郁」活動墨水手寫版

此輪保留「郁」字正確字形，再加入手寫墨水的不規則邊緣、輕微拖筆與速度感，避免前一版手繪筆畫過度變形。三版都維持視覺置中。

### A10. 活動墨水字

- 檔案：`assets/logo-options/option-a10-activity-ink-kai.png`
- 特色：更像講義手寫字，置中且清楚。
- 適合：想要最穩定、最不容易在 Google 小圖失真。

### A11. 俏皮墨水字

- 檔案：`assets/logo-options/option-a11-playful-ink-kai.png`
- 特色：筆畫更活潑，保留可讀性。
- 適合：想要比較有活動感、但不要太飛。

### A12. 飄逸墨水字

- 檔案：`assets/logo-options/option-a12-flowing-ink-kai.png`
- 特色：更有速度感，已修正置中。
- 適合：想要更接近手寫情緒與流動感。

### A 活動墨水手寫版預覽

- 總覽圖：`assets/logo-options/option-a-activity-ink-preview.png`
