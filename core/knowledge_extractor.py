import requests
from bs4 import BeautifulSoup

def extract_code_from_url(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        blocks = soup.find_all(["pre", "code"])
        return [b.get_text().strip() for b in blocks if "def " in b.text or "import" in b.text]
    except:
        return []
