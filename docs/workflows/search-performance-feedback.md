# 工作流：Search Console 索引與搜尋成效回饋

更新日期：2026-07-25

## 觸發與負責角色

- 觸發：新頁發布、SEO 文案更新、sitemap 變更、固定月度／季度回顧，或使用者要求檢查 Google 搜尋成效。
- 統籌：網站總管 AI。
- 執行：搜尋成效與索引驗收 AI。
- 接收回饋：搜尋趨勢研究 AI、SERP／搜尋意圖分析 AI、內容機會策略 AI、內容編輯 AI、SEO／發布維護 AI。
- 審查：品質檢查 AI 檢查報告證據與結論強度。

## 權限邊界

- 讀取 Search Console、分析匯出 CSV 或使用者截圖屬於唯讀驗收。
- 提交 sitemap、執行 URL Inspection Live Test、Request indexing 或其他外部變更，必須由使用者明確授權。
- 沒有可用權限時，建立「待使用者提供」清單，不得杜撰資料或假裝已登入。
- 已要求建立索引、已在 Google 服務中或已編入索引的 URL，不重複送出申請。

## 總管需求單

必填：

- 目標 URL、發布／修改日期與對應 commit。
- 原始趨勢報告、SEO 需求單、目標讀者、目標 query cluster 與搜尋意圖。
- 基準期間與觀察期間；預設 28 天對前 28 天，並視樣本加入 7／90 天。
- 品牌詞／非品牌詞與目標詞的定義。
- Search Console 權限狀態。
- 允許執行的唯讀或外部變更範圍。
- 成功、部分成功、資料不足與負向訊號的判定方式。

## 索引台帳

每個目標 URL 記錄：

- URL、頁面類型、發布日期與最後修改日期。
- 是否在 sitemap、sitemap 提交／讀取狀態。
- Google 索引狀態與 Google-selected canonical。
- robots／noindex、上次檢索與 live test 狀態（若取得）。
- Request indexing 是否曾送出、送出日期與當時結果。
- 下一次允許檢查時間；避免無意義重複操作。

## 搜尋成效分析

至少分析：

- Total clicks、impressions、CTR、average position。
- Queries：目標詞、相關長尾詞、品牌詞、非品牌詞與非預期詞。
- Pages：目標頁及可能互搶頁。
- Country：以台灣為主要範圍。
- Device：桌面與手機差異（樣本足夠時）。
- Search appearance：若有適用資料。
- 期間比較：7／28／90 天，並記錄 preliminary 或低樣本限制。

平均排名是所有曝光的平均位置，不是單次或固定名次。判斷優先看曝光與點擊趨勢，再看 CTR、query mix 與 position。

## 策略驗證矩陣

### 趨勢策略回饋

比較：

- 預測的議題與 query cluster。
- 實際新增／成長的 Search Console queries。
- 目標頁曝光與點擊是否增長。
- 熱度是短期尖峰、季節性還是持續需求。

結論：

- `positive`：多個相關 query 與目標頁出現一致的正向訊號。
- `mixed`：部分命中，但 CTR、排名、頁面互搶或意圖仍需調整。
- `no_clear_change`：樣本不足或尚無明顯差異，繼續觀察。
- `negative`：目標 query／頁面顯著下降，且排除季節性、索引或資料問題後仍成立。

### SEO 文案回饋

比較：

- 需求單的 primary／secondary queries。
- 實際 query、頁面、曝光、點擊、CTR 與意圖。
- title／description 是否吸引正確查詢者。
- 內容是否被非預期 query 找到，是否代表新機會或意圖偏移。
- 是否有其他頁面承接同一 query，造成關鍵字互搶。

判定：

- `hit`：目標 query cluster 與目標頁出現可重現成效。
- `partial_hit`：相關長尾詞出現，但核心 query 或 CTR 尚未達成。
- `miss`：足夠觀察期後仍未出現目標 query，或實際意圖明顯不同。
- `insufficient_data`：索引時間、曝光或觀察期不足，不能下結論。

## 回饋與再派工

搜尋成效與索引驗收 AI 必須將同一份報告分流：

- 給搜尋趨勢研究 AI：哪些議題得到實際需求支持、哪些只是短期熱度。
- 給 SERP／搜尋意圖分析 AI：實際 query 是否和原判斷一致。
- 給內容機會策略 AI：更新／新增／文章群決策是否有效，是否需處理互搶。
- 給內容編輯 AI：文案實際命中的語句、意圖偏移與可改善區塊。
- 給 SEO／發布維護 AI：CTR、metadata、索引、canonical、sitemap 或結構化資料問題。
- 給網站總管 AI：維持、微調、重新研究、等待、回復或停止的建議。

總管只有在報告提出可執行方向、研究品質與品質檢查通過後，才能建立下一輪需求單。報告本身不授權修改網站。

## 建議頻率

- 發布後 7 天：確認索引與早期訊號，不以低樣本判定成敗。
- 發布後 28 天：第一次策略與文案成效回顧。
- 發布後 90 天：中期成效與常青／季節性判斷。
- 每月：全站 query／page 趨勢回饋。
- 每季：內容策略、關鍵字互搶與主題群回顧。

## 必要交付

- `docs/seo/search-performance/report-template.md` 格式的日期化報告。
- URL 索引台帳與已送出申請紀錄。
- 趨勢策略結果、SEO 文案命中結果、信心與資料限制。
- 分角色回饋與總管下一輪建議。

## 完成與停止條件

- 完成：資料期間、篩選條件、指標、結論與回饋對象可追溯，品質檢查通過。
- 停止：無權限、資料量不足、Search Console 資料尚未更新、目標策略未定義或外部操作未授權。
- 停止不等於失敗；狀態標記 `blocked` 或 `insufficient_data`，列出需要的資料與下次檢查時間。
