from fastapi import APIRouter
from utils.agent_manager import create_agent, assign_task, get_agent_logs

agent_collab_router = APIRouter()

@agent_collab_router.post("/create")
def spawn_agent(name: str, goal: str):
    return create_agent(name, goal)

@agent_collab_router.post("/task")
def send_task(agent: str, task: str):
    return assign_task(agent, task)

@agent_collab_router.get("/logs")
def all_logs():
    return get_agent_logs()


@agent_collab_router.post("/discuss")
def agent_debate(agent_a: str, agent_b: str, topic: str):
    from utils.agent_manager import debate_agents
    return debate_agents(agent_a, agent_b, topic)

@agent_collab_router.post("/score")
def score_agent(agent: str, outcome: str):
    from utils.agent_manager import score_agent_decision
    return score_agent_decision(agent, outcome)

@agent_collab_router.get("/reflection")
def agent_team_reflection():
    from utils.agent_manager import reflect_as_team
    return reflect_as_team()
