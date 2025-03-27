import ast

def check_reasoning_paths(file_path):
    print(f"🛠️ Checking Reasoning Paths in {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        tree = ast.parse(code)

        decision_points = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.Match)):
                decision_points += 1

        print(f"[✓] Reasoning Paths Detected: {decision_points}")
        if decision_points == 0:
            print("[⚠️] No decision points found. Logic may be static.")
    except Exception as e:
        print(f"[✗] Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter Python file path to check reasoning paths: ")
    check_reasoning_paths(file_path)
