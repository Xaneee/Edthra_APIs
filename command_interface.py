from fastapi import APIRouter
from utils.command_router import process_command
from utils.voice_engine import speak

command_router = APIRouter()

@command_router.get("/command")
def run_command(input: str):
    response = process_command(input)
    speak(response["response"])
    return response
