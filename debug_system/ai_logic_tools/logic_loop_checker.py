import ast

def detect_infinite_loops(file_path):
    print(f"🔎 Detecting Infinite Loops in {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.While) and isinstance(node.test, ast.Constant) and node.test.value is True:
                print("[⚠️] Potential Infinite Loop Detected!")
        print("[✓] Loop Check Complete.")
    except Exception as e:
        print(f"[✗] Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter Python file path to check for loops: ")
    detect_infinite_loops(file_path)
