from utils.code_mutator import safely_mutate_code

def validate_code_block(code, file_path=None):
    issues = []
    fixes = []

    if "eval(" in code:
        issues.append("⚠️ Use of eval() is unsafe.")
        fixes.append("Replace 'eval()' with a safe parser or avoid dynamic execution.")

    if "os.system" in code:
        issues.append("⚠️ os.system used — check for command injection.")
        if file_path:
            safely_mutate_code(file_path, "os.system", "# os.system (disabled for safety)")

    if "while True" in code and "break" not in code:
        issues.append("⚠️ Infinite loop without break.")
        fixes.append("Add a break condition to prevent infinite loop.")

    if "password" in code and "=" in code:
        issues.append("⚠️ Hardcoded password found.")
        fixes.append("Move password to .env file or secure vault.")

    return {
        "issues": issues if issues else ["✅ No obvious issues."],
        "fixes": fixes if fixes else ["No auto-fix needed."]
    }
