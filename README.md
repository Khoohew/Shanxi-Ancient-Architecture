# 山西古建檔案庫
**Shanxi Ancient Architecture**

山西省 11 個地級市、449 處古建築與遺存的資料庫：年代、文保級別、看點，以及可追溯的來源。

## 👀 我只想瀏覽（給人看）

| 想做什麼 | 入口 |
|---|---|
| **按城市展開、搜尋、一鍵地圖定位**（推薦） | [瀏覽頁面](https://khoohew.github.io/Shanxi-Ancient-Architecture/)（需開啟 GitHub Pages，見下方說明） |
| 看精簡表格（只有 8 列，可直接在 GitHub 打開） | [sites-simple.csv](data/sites-simple.csv) |
| 按城市看景點與級別（純文字版） | [城市地點索引](data/city-index.md) |
| 看某處詳細研究（建築形制、年代爭議、來源） | [古建研究檔案](places/README.md) |
| 在 Google 地圖看全部點位 | [Google My Maps 導入指南](maps/google-mymaps.md) |

> 在瀏覽頁面點開景點後，按「📍 在地圖定位」會直接在 Google 地圖跳到該點，不需要自己搜尋。地圖座標是原始標記，可能有偏移，請以現場為準。

## 🔧 資料維護與 AI 工具（給維護者／AI 看）

<details>
<summary>展開</summary>

| 內容 | 入口 |
|---|---|
| 完整資料表（15 列，含來源、備註） | [sites.csv](data/sites.csv) · [sites.json](data/sites.json) |
| 欄位說明 | [資料欄位說明](data/data-dictionary.md) |
| 研究進度與批次 | [研究進度](research-progress.md) |
| 尚待核實的點位與缺口 | [待核清單](data/pending-verification.md) |
| 資料來源與研究規範 | [資料來源與研究規範](sources/README.md) |
| 貢獻與修改規則 | [CONTRIBUTING](CONTRIBUTING.md) |
| 用 AI 輔助查詢與規劃行程 | [倉庫使用指南](itineraries/how-to-use-this-repository-with-chatgpt.md) |
| 重新生成瀏覽頁面與精簡表 | `python3 tools/build_site.py`（修改 sites.csv 後執行） |

</details>

## 目前進度

- 449 處點位：已覈實 3、部分覈實 444、待覈實 2。
- 「部分覈實」＝朝代有可靠來源，但分殿年代、維修史未查清。
- 資料以桌面文獻核查為主，**不等於現場踏查**。開放時間、預約、票價請出發前自行核實。

## 研究原則

1. 分清不同年代：寺院始建、現存殿堂、塑像／壁畫、歷代維修分開記錄。
2. 來源可追溯：優先政府名錄、文物部門、博物館、高校、正式調查與學術出版。
3. 保留爭議：來源矛盾時並列說法，不為單一年代刪除異說。
4. 座標不擅改：保留原始座標；不宣稱座標基準已驗證。
5. 不推定可進入：地圖標記不代表開放、可入內或可登塔。

## 資料說明

- 原始位置線索來自使用者提供的 [Bilibili 影片（BV12eYXeTE2A）](https://www.bilibili.com/video/BV12eYXeTE2A)。
- 449 是地理標記數，不等於 449 處均為文保單位。
- `source_confidence` 是資料證據成熟度，不是文保級別。

---

資料修訂請經 Pull Request 進入 `main`，並附可追溯來源與核查日期。
