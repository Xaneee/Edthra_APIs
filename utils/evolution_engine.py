import random

def evolve_logic(target):
    changes = {
        "reasoning": [
            ("To build an API,", "APIs must include strong validation."),
            ("I must read the file", "I must back up the file before mutation."),
        ],
        "validator": [
            ("eval(", "# eval() is blocked for safety."),
            ("os.system", "# os.system replaced with subprocess.run")
        ]
    }

    file_map = {
        "reasoning": "utils/reasoning_engine.py",
        "validator": "utils/validator_engine.py"
    }

    if target not in changes or target not in file_map:
        return {"error": "Invalid evolution target."}

    path = file_map[target]
    try:
        with open(path, "r") as f:
            lines = f.readlines()

        replaced = False
        for old, new in changes[target]:
            for i, line in enumerate(lines):
                if old in line:
                    lines[i] = line.replace(old, new)
                    replaced = True
                    break
            if replaced:
                break

        if replaced:
            with open(path, "w") as f:
                f.writelines(lines)
            return {"status": "success", "mutation": f"{old} → {new}", "file": path}
        else:
            return {"status": "no change", "message": "Target pattern not found."}

    except Exception as e:
        return {"error": str(e)}
