# 山西古建檔案庫
**Shanxi Ancient Architecture**

面向山西實地訪古與建築史研究的資料庫。收錄山西省 11 個地級市、449 處原始地圖點位，持續補充古建年代、建築形制、彩塑壁畫、文物保護身份與可追溯來源。

## 快速入口

| 需求 | 直接入口 |
|---|---|
| 按城市查找 449 處地點及文物保護級別 | [城市地點索引](data/city-index.md) |
| 原始資料、座標與研究欄位 | [CSV 資料表](data/sites.csv) · [JSON 資料](data/sites.json) |
| 全部地點地圖 | [完整 KML](maps/all-sites.kml) |
| 按城市查看地圖 | [城市 KML 索引](data/city-index.md) |
| 查閱古建逐點研究 | [古建研究檔案索引](places/README.md) |
| 研究進度與下一批 | [研究進度](research-progress.md) |
| 尚待核實的點位與缺口 | [待核清單](data/pending-verification.md) |
| 資料欄位說明 | [資料欄位說明](data/data-dictionary.md) |
| 資料來源與研究規範 | [資料來源與研究規範](sources/README.md) |
| Google My Maps 導入 | [Google My Maps 導入指南](maps/google-mymaps.md) |
| 使用 AI 輔助查詢與規劃 | [倉庫使用指南](itineraries/how-to-use-this-repository-with-chatgpt.md) |
| 資料貢獻與修改規則 | [資料貢獻與修改規則](CONTRIBUTING.md) |

## 目前進度

- 地圖底庫：449 處地點，分布於 11 個地級市。
- 逐點研究：各市分批進行，詳細完成範圍及待核問題見 [研究進度頁](research-progress.md)。
- 下一批研究編號以研究進度頁及 [研究檔案索引](places/README.md) 的最新記錄為準。

## 研究原則

1. **分清不同年代**：寺院始建、現存殿堂建造、塑像／壁畫製作及歷代維修分開記錄。
2. **來源可追溯**：優先使用政府文物名錄、文物主管部門、博物館、高校、正式調查報告及學術出版物。
3. **保留爭議**：來源矛盾時並列說法與依據，不為了給出單一年代而刪除異說。
4. **座標不擅改**：保留原始地圖座標；未完成專業轉換前，不宣稱座標基準已驗證。
5. **不推定可進入**：地圖標記不代表開放、可入內或可登塔；學校、村院及看護區域須另行聯絡確認。

## 資料說明

- 原始位置線索來自使用者提供的 [Bilibili 影片（BV12eYXeTE2A）](https://www.bilibili.com/video/BV12eYXeTE2A)，再整理為 CSV、JSON 與 KML。
- 449 是地理標記數，不等於 449 處均為文物保護單位，也不代表所有地點均已完成斷代或現場核實。
- `source_confidence` 是桌面資料證據等級，不是文物保護級別；A 也不代表現場踏查完成。
- 開放時間、票價、預約、道路及維修狀態會變動，出發前須重新核查。

---

建議所有資料修訂經 Pull Request 進入 `main`。研究檔案以繁體中文維護；新增斷代與開放資訊時，請附上可追溯來源及核查日期。
