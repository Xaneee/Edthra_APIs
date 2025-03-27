from fastapi import APIRouter
from utils.local_searcher import local_doc_search
from utils.local_knowledge import offline_answer

offline_router = APIRouter()

@offline_router.get("/offline/search")
def search_local_docs(query: str):
    return local_doc_search(query)

@offline_router.get("/offline/ask")
def ask_offline_brain(question: str):
    return offline_answer(question)
