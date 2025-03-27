import os
import requests

def fetch_remote_patch(url):
    r = requests.get(url)
    if r.status_code == 200:
        with open("core/edithra_agi.py", "w") as f:
            f.write(r.text)
        return "[✓] Edithra updated from remote source."
    return "[!] Update failed."

# Usage: fetch_remote_patch("https://raw.githubusercontent.com/user/repo/main/core/edithra_agi.py")
