import os
import email
from email.policy import default
import pandas as pd
import re
from tqdm import tqdm

# 設定你的根目錄資料夾
root_folder = r"{your_path}"

# 初始化清單
contact_records = []

# 提取email地址與名字的正則表達式
email_regex = re.compile(r'(.*?)([\w\.-]+@[\w\.-]+)')

# 收集所有eml檔案路徑
# 收集所有eml檔案路徑
eml_files = []
for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.lower().endswith(".eml"):
            eml_files.append(os.path.join(root, file))

if not eml_files:
    print(f"找不到任何 .eml 檔案在 {root_folder} 下面，請確認路徑！")
    exit()

print(f"總共找到 {len(eml_files)} 個eml檔案，開始解析...")

# 開始讀取
for eml_path in tqdm(eml_files):
    try:
        with open(eml_path, "rb") as f:
            msg = email.message_from_binary_file(f, policy=default)
            for header in ['From', 'To', 'Cc', 'Bcc']:
                header_value = msg.get(header)
                if header_value:
                    entries = header_value.split(",")
                    for entry in entries:
                        entry = entry.strip()
                        match = email_regex.search(entry)
                        if match:
                            name = match.group(1).strip(' "\'<>') if match.group(1) else ""
                            address = match.group(2).strip()
                            relative_path = os.path.relpath(eml_path, root_folder)
                            contact_records.append({
                                "DisplayName": name,
                                "Email": address,
                                "Source": header,
                                "EML_File": relative_path
                            })
    except Exception as e:
        print(f"檔案 {eml_path} 解析失敗，錯誤訊息：{e}")

# 轉成DataFrame
df = pd.DataFrame(contact_records)

# 去除Email + Source 重複的（有些信可能重複寄）
df.drop_duplicates(subset=["Email", "Source"], inplace=True)

# 排序
df = df.sort_values(by=["Email", "Source"])

# 輸出CSV
output_path = os.path.join(root_folder, "contract.csv")
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"\n完成！共整理出 {len(df)} 筆記錄。")
print(f"結果已儲存在：{output_path}")
