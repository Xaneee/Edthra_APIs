import random
import time

def detect_anomalies():
    print("🤖 Detecting Anomalies in System Activity...")
    time.sleep(1)
    # Simulated anomaly detection (in production, this would use actual data)
    anomalies_detected = random.choice([True, False])

    if anomalies_detected:
        print("[⚠️] Anomaly Detected! Potential Malicious Activity.")
    else:
        print("[✓] No Anomalies Detected. System Secure.")

if __name__ == "__main__":
    detect_anomalies()
