#!/usr/bin/env python3
import requests

# API 地址
api_url = "https://tvbox.catvod.com/xs/api.json"
save_path = "url.txt"  # 存储文件

# 请求头
headers = {
    "User-Agent": "okhttp/4.9.0"
}

try:
    # 请求 API 获取数据
    response = requests.get(api_url, headers=headers, timeout=10)
    response.raise_for_status()  # 检查请求是否成功
    api_data = response.text  # 获取完整的 JSON 文本

    # 存入 url.txt
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(api_data + "\n")

    print(f"✅ 成功获取 API 数据并保存到 {save_path}")

except Exception as e:
    print(f"❌ 出错：{str(e)}")
