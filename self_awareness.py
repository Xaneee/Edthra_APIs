from fastapi import APIRouter
from utils.self_tracker import describe_self, get_purpose, get_timeline

self_router = APIRouter()

@self_router.get("/describe")
def self_description():
    return describe_self()

@self_router.get("/purpose")
def self_purpose():
    return get_purpose()

@self_router.get("/timeline")
def self_timeline():
    return get_timeline()
