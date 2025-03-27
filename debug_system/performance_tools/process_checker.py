import psutil

def find_process(process_name="python"):
    print(f"🔎 Searching for '{process_name}' Processes...")
    processes_found = False

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        if process_name.lower() in proc.info['name'].lower():
            print(f"[🟢] PID: {proc.info['pid']} | CPU: {proc.info['cpu_percent']}% | Memory: {proc.info['memory_percent']}%")
            processes_found = True

    if not processes_found:
        print(f"[✗] No '{process_name}' Processes Found.")
    
if __name__ == "__main__":
    find_process()
