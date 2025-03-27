from fastapi import APIRouter
from core.self_trainer import learn_topic

learn = APIRouter()

@learn.post("/learn/topic")
def learn_web(topic: str):
    return {"result": learn_topic(topic)}
