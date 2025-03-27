import os
import subprocess

def deploy_to_git(git_repo: str):
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Auto deploy from Edithra AGI"')
    os.system(f"git remote add origin {git_repo}")
    os.system("git branch -M main")
    os.system("git push -u origin main")
    print("[✓] Pushed to GitHub. Ready for Railway/Vercel deployment.")

# Usage:
# deploy_to_git("https://github.com/your-user/edithra-agi")
