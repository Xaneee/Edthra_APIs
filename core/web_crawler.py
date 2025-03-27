import requests
from bs4 import BeautifulSoup
from utils.url_cleaner import clean_url

def crawl_search(query: str):
    url = f"https://duckduckgo.com/html?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [clean_url(a['href']) for a in soup.select(".result__title a") if "href" in a.attrs]
    return links[:5]
