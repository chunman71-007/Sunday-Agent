name: Generate Sunday Sticker

on:
workflow_dispatch:
inputs:
style:
description: 贴纸样式
required: true
default: new_year
text:
description: 祝福语文字
required: false
default: 'Happy Meow Year'

jobs:
generate:
runs-on: ubuntu-latest
steps:
- name: 拉取代码
uses: actions/checkout@v3

- name: 设置 Python 环境
uses: actions/setup-python@v4
with:
python-version: '3.10'

- name: 安装依赖（如有）
run: pip install -r requirements.txt || echo "没有找到依赖文件"

- name: 生成贴纸
run: |
python src/generate_sticker.py
