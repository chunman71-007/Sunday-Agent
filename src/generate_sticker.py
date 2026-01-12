# generate_sticker.py

import os
from datetime import datetime

# 模擬貼圖生成函數
def create_sticker(style="new_year", text="Happy Meow Year", output_dir="assets/generated"):
# 建立輸出資料夾（如未存在）
os.makedirs(output_dir, exist_ok=True)

# 模擬貼圖檔案名稱
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{style}_sticker_{timestamp}.txt"
filepath = os.path.join(output_dir, filename)

# 模擬貼圖內容（實際可改為圖像生成）
content = f"""
🐾 Sunday Agent 貼圖生成
風格：{style}
文字：{text}
時間：{timestamp}
"""

# 寫入檔案
with open(filepath, "w", encoding="utf-8") as f:
f.write(content.strip())

print(f"✅ 貼圖已生成：{filepath}")

# 主程式入口
if __name__ == "__main__":
# 你可以在這裡改變風格與文字
create_sticker(style="birthday", text="Happy Purr-thday!")
