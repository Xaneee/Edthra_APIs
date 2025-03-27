from fastapi import APIRouter
import json

store = APIRouter()

@store.get("/store/list")
def list_apps():
    with open("core/store_db.json", "r") as f:
        return json.load(f)

@store.post("/store/add")
def add_app(title: str, description: str, path: str):
    with open("core/store_db.json", "r+") as f:
        data = json.load(f)
        data.append({
            "title": title,
            "description": description,
            "price": "Free",
            "path": path,
            "status": "active"
        })
        f.seek(0)
        json.dump(data, f, indent=2)
    return {"message": "App added to Edithra Store"}


@store.post("/store/price")
def update_price(path: str, new_price: str):
    with open("core/store_db.json", "r+") as f:
        data = json.load(f)
        for app in data:
            if app["path"] == path:
                app["price"] = new_price
                break
        f.seek(0)
        json.dump(data, f, indent=2)
    return {"message": "Price updated."}
