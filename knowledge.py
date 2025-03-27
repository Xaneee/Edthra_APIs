from fastapi import APIRouter
from utils.web_searcher import search_web

knowledge_router = APIRouter()

@knowledge_router.post("/query")
def query_web(search: str):
    result = search_web(search)
    return {"query": search, "results": result}
