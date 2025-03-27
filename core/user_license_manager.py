import uuid
import json
import os

LICENSES = "core/licenses.json"

def issue_license(app_title, user_email):
    os.makedirs("core", exist_ok=True)
    if not os.path.exists(LICENSES):
        with open(LICENSES, "w") as f:
            json.dump([], f)

    with open(LICENSES, "r+") as f:
        data = json.load(f)
        key = str(uuid.uuid4())
        data.append({
            "app": app_title,
            "email": user_email,
            "license": key
        })
        f.seek(0)
        json.dump(data, f, indent=2)
    return key
