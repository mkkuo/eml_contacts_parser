📩 EML Contacts Parser
這是一個用於批次解析 .eml 郵件檔案中的聯絡人資訊的小工具，能自動提取寄件人、收件人、副本等欄位中的姓名與電子郵件地址，並匯出為結構化的 CSV 檔案。

🚀 功能特色
遞迴搜尋目錄下所有 .eml 檔案
分析 From、To、Cc、Bcc 欄位
自動清理重複的 Email + 欄位組合
匯出聯絡人資訊至 contract.csv

📂 專案結構
.
├── eml_contacts_parser.py    # 主程式
├── your_eml_folder/          # 放置 .eml 郵件檔案的資料夾
└── contract.csv              # 執行後產生的聯絡人清單

🛠 使用方式
安裝必要套件：
pip install pandas tqdm

修改程式中 root_folder 的變數，指定為 .eml 檔案所在的資料夾：
root_folder = r"D:\your\eml\folder\path"

執行腳本：
python eml_contacts_parser.py
產生的 contract.csv 將會包含以下欄位：

DisplayName	Email	Source	EML_File
John Smith	john@example.com	To	email_folder/mail1.eml

📌 注意事項
僅處理 .eml 檔案格式。
請確保郵件中有標準格式的 From、To、Cc 或 Bcc 欄位。
若有錯誤將會列出在命令列中，但不會中斷整體流程。

📄 授權
本工具以 MIT 授權方式釋出，自由使用、修改與散布。
