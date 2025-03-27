from fastapi import APIRouter
from core.marketplace_engine import list_paid_apps, get_app_info
from core.user_license_manager import issue_license

market = APIRouter()

@market.get("/market/apps")
def get_paid_apps():
    return list_paid_apps()

@market.get("/market/info")
def app_info(name: str):
    return get_app_info(name)

@market.post("/market/buy")
def buy_app(name: str, email: str):
    return {"license": issue_license(name, email)}
