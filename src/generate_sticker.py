import os
import sys
from datetime import datetime

def create_sticker(style="new_year", text="Happy Meow Year", output_dir="assets/generated"):
os.makedirs(output_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
filename = f"{style}_sticker_{timestamp}.txt"
filepath = os.path.join(output_dir, filename)

content = f"""
🐱 Sunday Agent 貼紙生成器
樣式: {style}
文字: {text}
時間: {timestamp}
"""

with open(filepath, "w", encoding="utf-8") as f:
f.write(content.strip())

print(f"貼紙已儲存至: {filepath}")
print(f"實際收到 style: '{style}'")
print(f"實際收到 text: '{text}'")

if __name__ == "__main__":
print("sys.argv:", sys.argv)

style = sys.argv[1] if len(sys.argv) > 1 else "new_year"
text = sys.argv[2] if len(sys.argv) > 2 else "Happy Meow Year"
create_sticker(style=style, text=text)
