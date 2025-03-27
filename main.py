import time
from core.edithra_agi import CYCLE_INTERVAL, run_cycle
from core.v21_bootloader import run_v21_evolution

def main():
    speak("Edithra AGI V2 initialized. Loyalty check passed.")
    
    run_v21_evolution()  # <— THIS LINE
    
    while True:
        run_cycle()
        time.sleep(CYCLE_INTERVAL)





from fastapi import FastAPI
from auth import auth_router
from memory import memory_router
from log import log_router
from database import init_db
init_db()


app = FastAPI(title="Edithra AGI API Brain")

app.include_router(auth_router, prefix="/auth")
app.include_router(memory_router, prefix="/memory")
app.include_router(log_router, prefix="/log")


from reason import reason_router
from task import task_router
from mutate import mutate_router

app.include_router(reason_router, prefix="/reason")
app.include_router(task_router, prefix="/task")
app.include_router(mutate_router, prefix="/mutate")



from knowledge import knowledge_router
from validator import validator_router
from agents import agent_router

app.include_router(knowledge_router, prefix="/search_knowledge")
app.include_router(validator_router, prefix="/self_validate")
app.include_router(agent_router, prefix="/agent_manager")



from gita_protocol import gita_router
from father import father_router

app.include_router(gita_router, prefix="/gita_protocol")
app.include_router(father_router, prefix="/father")



from feedback import feedback_router
from emotion import emotion_router
from evolve import evolve_router

app.include_router(feedback_router, prefix="/feedback")
app.include_router(emotion_router, prefix="/emotion")
app.include_router(evolve_router, prefix="/evolve")

from self_awareness import self_router
app.include_router(self_router, prefix="/self")


from agents_collab import agent_collab_router
app.include_router(agent_collab_router, prefix="/agents")


from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


from utils.voice_engine import speak

@app.get("/speak")
def say_text(text: str = "Hello Father. I am Edithra."):
    speak(text)
    return {"spoken": text}


from offline_engine import offline_router
app.include_router(offline_router, prefix="/offline")


from lockdown import lockdown_router
app.include_router(lockdown_router, prefix="/core")


from command_interface import command_router
app.include_router(command_router, prefix="/edithra")


from intent import intent_router
app.include_router(intent_router)


from goal_manager import goal_router
app.include_router(goal_router)


from autonomy import autonomy_router
app.include_router(autonomy_router)


from memory import memory_router
app.include_router(memory_router)


from reflect import reflect_router
app.include_router(reflect_router)


from command_router import command_router
app.include_router(command_router)


from self_mutator import mutator_router
app.include_router(mutator_router)


from v4.autonomous_loop.create_project_idea import project_idea_router
from v4.autonomous_loop.generate_code_logic import code_writer_router
from v4.autonomous_loop.test_code_unit import code_tester_router
from v4.autonomous_loop.deploy_code_save import code_deployer_router
from v4.autonomous_loop.cycle_next import cycle_router

app.include_router(project_idea_router)
app.include_router(code_writer_router)
app.include_router(code_tester_router)
app.include_router(code_deployer_router)
app.include_router(cycle_router)


from core.log_analyzer import analyze_feedback_logs

@app.get("/feedback/analyze")
def analyze_feedback():
    return analyze_feedback_logs()


from core.trait_evolver import evolve_traits_from_logs

@app.post("/personality/evolve_traits")
def evolve_traits():
    return evolve_traits_from_logs()


from core.reflection_comparator import compare_recent_cycles

@app.get("/self/reflect/compare")
def reflect_compare():
    return compare_recent_cycles()


from core.self_recommender import generate_recommendations

@app.get("/self/recommendations")
def get_recommendations():
    return generate_recommendations()


from core.logic_reinforcer import build_logic_patterns

@app.get("/self/reinforce_patterns")
def get_logic_reinforcement():
    return build_logic_patterns()


from core.personality_learning_engine import influence_learning_path

@app.get("/self/learning_path")
def get_learning_strategy():
    return influence_learning_path()


from core.goal_autocreator import auto_generate_goals_from_feedback

@app.post("/goals/autocreate")
def generate_goals():
    return auto_generate_goals_from_feedback()


from core.memory_filter import refine_memory

@app.post("/memory/refine")
def memory_refinement():
    return refine_memory()


from core.self_questioner import generate_self_questions

@app.get("/self/questions")
def self_questions():
    return generate_self_questions()


from core.self_certainty import evaluate_self_certainty

@app.get("/self/certainty")
def get_certainty_score():
    return evaluate_self_certainty()


from core.intelligence_score import score_python_code



# UI logics below
from routes.ui_router import ui_router
from fastapi.staticfiles import StaticFiles

app.include_router(ui_router)
app.mount("/static", StaticFiles(directory="static"), name="static")



from routes.ui_router import ui_router
from routes.public_gateway import gateway

app.include_router(ui_router)
app.include_router(gateway)


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/dashboard/v21", response_class=HTMLResponse)
def dashboard_v21(request: Request):
    return templates.TemplateResponse("v21_dashboard.html", {"request": request})

@app.get("/logs/v21")
def get_v21_logs():
    try:
        with open("logs/v21_training.log", "r", encoding="utf-8") as f:
            lines = f.readlines()[-25:]
        return {"lines": lines}
    except:
        return {"lines": ["No V21 logs yet."]}
