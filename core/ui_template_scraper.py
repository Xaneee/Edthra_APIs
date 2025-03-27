import requests
from bs4 import BeautifulSoup

def fetch_ui_templates(query="dashboard html template"):
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [a["href"] for a in soup.select(".result__title a") if "href" in a.attrs]
    return links[:5]
