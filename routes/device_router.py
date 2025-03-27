from fastapi import APIRouter
from core.os_bridge import system_info, run_terminal_command
from core.iot_linker import simulate_device_action

device = APIRouter()

@device.get("/device/info")
def get_os_info():
    return system_info()

@device.post("/device/exec")
def exec_cmd(cmd: str):
    return {"output": run_terminal_command(cmd)}

@device.post("/device/simulate")
def simulate(device: str, action: str):
    return {"result": simulate_device_action(device, action)}
