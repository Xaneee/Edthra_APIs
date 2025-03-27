import ast

def analyze_logic_flow(file_path):
    print(f"🧠 Analyzing Logic Flow in {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        tree = ast.parse(code)
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

        print("[✓] Functions Detected:")
        for name in function_names:
            print(f" - {name}")

        if not function_names:
            print("[⚠️] No functions found. Check for logic errors.")
    except Exception as e:
        print(f"[✗] Error analyzing file: {e}")

if __name__ == "__main__":
    file_path = input("Enter Python file path to analyze: ")
    analyze_logic_flow(file_path)
