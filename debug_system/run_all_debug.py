import subprocess

# List of all debug commands
debug_commands = [
    "python debug_system/system_tools/system_health_check.py",
    "python debug_system/system_tools/file_integrity_check.py",
    "python debug_system/system_tools/log_analyzer.py",
    "python debug_system/system_tools/service_status_check.py",
    "python debug_system/network_tools/api_connection_tester.py",
    "python debug_system/network_tools/port_checker.py",
    "python debug_system/network_tools/network_latency_checker.py",
    "python debug_system/deployment_tools/docker_checker.py",
    "python debug_system/deployment_tools/container_checker.py",
    "python debug_system/deployment_tools/deployment_log_checker.py",
    "python debug_system/deployment_tools/environment_checker.py",
    "python debug_system/network_tools/firewall_checker.py"
]

def run_command(command):
    print(f"\n[🔎] Running: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[⚠️] Error: {e}")

def main():
    print("🚀 Starting Full Debug Sequence...\n")
    for command in debug_commands:
        run_command(command)
    print("\n✅ Debug Process Completed.")

if __name__ == "__main__":
    main()
