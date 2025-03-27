import json

MARKET_FILE = "core/store_db.json"

def list_paid_apps():
    with open(MARKET_FILE, "r") as f:
        data = json.load(f)
        return [a for a in data if a["price"] != "Free"]

def get_app_info(name):
    with open(MARKET_FILE, "r") as f:
        data = json.load(f)
        for app in data:
            if app["title"].lower() == name.lower():
                return app
    return None
