import psutil
import time

def monitor_resources(interval=2):
    print("🧑‍💻 Monitoring CPU and Memory Usage...")
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()

            print(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_info.percent}%")
            
            if cpu_percent > 85:
                print("[⚠️] High CPU Usage Detected!")
            if memory_info.percent > 85:
                print("[⚠️] High Memory Usage Detected!")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("[✓] Monitoring Stopped")

if __name__ == "__main__":
    monitor_resources()
