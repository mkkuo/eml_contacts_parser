# 📩 EML Contacts Parser

一個用來批次解析 `.eml` 郵件檔案的工具，可自動擷取收件人與寄件人等聯絡資訊，並匯出為 CSV 檔案。

---

## ✨ 功能特色

- 遞迴掃描資料夾中的 `.eml` 郵件檔案
- 擷取 `From`、`To`、`Cc`、`Bcc` 欄位中的 Email 與顯示名稱
- 自動去除重複聯絡人（Email + 來源欄位）
- 匯出結果至 `contract.csv`

---

## 📁 專案結構

```
.
├── eml_contacts_parser.py     # 主程式
├── example.eml                # 範例郵件（可選）
├── contract.csv               # 產出結果
└── README.md
```

---

## ⚙️ 安裝方式

先安裝必要套件：

```bash
pip install pandas tqdm
```

---

## 🚀 使用方式

1. 修改程式中的 `root_folder` 變數：

```python
root_folder = r"D:\your\eml\folder\path"
```

2. 執行腳本：

```bash
python eml_contacts_parser.py
```

3. 完成後會在原資料夾中生成 `contract.csv`，內容如下：

| DisplayName | Email             | Source | EML_File               |
|-------------|-------------------|--------|------------------------|
| John Smith  | john@example.com  | To     | email_folder/mail1.eml |

---

## 📝 注意事項

- 僅處理 `.eml` 格式的郵件
- 請確認信件含有標準格式的 `From`、`To`、`Cc` 或 `Bcc` 欄位
- 錯誤訊息會顯示於命令列中，不會中斷流程

---

## 📦 套件清單 (`requirements.txt`)

```
pandas
tqdm
```

---

## 📄 授權

本專案採用 MIT License 授權。
