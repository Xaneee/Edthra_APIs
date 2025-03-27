import os

def safely_mutate_code(file_path, target_line, new_line):
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        replaced = False
        for i in range(len(lines)):
            if target_line in lines[i]:
                lines[i] = lines[i].replace(target_line, new_line)
                replaced = True
                break

        if replaced:
            with open(file_path, "w") as f:
                f.writelines(lines)
            return {"status": "success", "message": "Line mutated."}
        else:
            return {"status": "failed", "message": "Target line not found."}
    except Exception as e:
        return {"error": str(e)}
