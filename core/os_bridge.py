import os
import platform

def system_info():
    return {
        "os": platform.system(),
        "version": platform.version(),
        "architecture": platform.machine()
    }

def run_terminal_command(command: str):
    try:
        output = os.popen(command).read()
        return output.strip()
    except Exception as e:
        return f"Error: {str(e)}"
