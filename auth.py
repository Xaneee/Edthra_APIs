from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.jwt_handler import create_token, decode_token
from database import get_db

auth_router = APIRouter()
security = HTTPBasic()

@auth_router.post("/login")
def login(credentials: HTTPBasicCredentials):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (credentials.username, credentials.password))
    user = cur.fetchone()
    if user:
        return {"token": create_token({"username": credentials.username})}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@auth_router.post("/verify")
def verify_token(token: str):
    user = decode_token(token)
    return {"valid": bool(user), "user": user}
