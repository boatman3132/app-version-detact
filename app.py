from google_play_scraper import app as google_play_app
import requests
import json

def get_google_play_version(package_name):
    """取得 Google Play 應用程式的最新版本號"""
    try:
        result = google_play_app(package_name)
        return result["version"]
    except Exception as e:
        return f"查詢失敗: {e}"

def get_app_store_version(app_id, country="tw"):
    """取得 App Store 應用程式的最新版本號"""
    url = f"https://itunes.apple.com/{country}/lookup?id={app_id}"
    response = requests.get(url)
    data = response.json()
    if data["resultCount"] > 0:
        return data["results"][0]["version"]
    return "未找到應用程式"

# 設定應用程式清單
apps = [
    {
        "name": "EZ WAY 易利委",
        "google_play_package": "com.tradevan.android.forms",
        "app_store_id": "1127781971"
    },
    {
        "name": "蝦皮購物 Shopee",
        "google_play_package": "com.shopee.tw",
        "app_store_id": "959841107"
    },
    {
        "name": "淘寶購物",
        "google_play_package": "com.taobao.taobao",
        "app_store_id": "387682726"
    }
]

# 查詢並儲存結果
results = []
for app in apps:
    google_version = get_google_play_version(app["google_play_package"])
    ios_version = get_app_store_version(app["app_store_id"])

    results.append({
        "name": app["name"],
        "google_play_version": google_version,
        "app_store_version": ios_version
    })

# 將結果寫入 JSON 檔案
with open("app_versions.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("已將最新版本號資訊寫入 app_versions.json 檔案")
