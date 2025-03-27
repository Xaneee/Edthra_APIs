import os

def check_env_variables(required_vars):
    print("🔎 Checking Environment Variables...")
    missing_vars = []
    for var in required_vars:
        if os.getenv(var) is None:
            print(f"[⚠️] Missing: {var}")
            missing_vars.append(var)
        else:
            print(f"[✓] Found: {var} - {os.getenv(var)}")
    return missing_vars

if __name__ == "__main__":
    required_vars = input("Enter required environment variables separated by commas: ").split(",")
    missing = check_env_variables([v.strip() for v in required_vars])
    if missing:
        print("[✗] Some environment variables are missing.")
    else:
        print("[✓] All environment variables are present.")
