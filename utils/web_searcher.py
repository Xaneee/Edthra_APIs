import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; EdithraBot/1.0; +https://edithra.ai)"
}

def try_extract_code(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        code_blocks = soup.find_all(["code", "pre"])

        for block in code_blocks:
            code = block.get_text().strip()
            if "import" in code or "def " in code:
                return code[:300] + "..." if len(code) > 300 else code
    except:
        return "⚠ Could not extract code."
    return "❌ No code block found."

def search_web(query):
    results = []
    try:
        ddg_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}+python"
        res = requests.get(ddg_url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".result__title a")

        for link in links[:5]:
            href = link.get("href")
            if "github.com" in href or "stackoverflow.com" in href or "medium.com" in href or "dev.to" in href:
                code_snippet = try_extract_code(href)
                if "def " in code_snippet or "import" in code_snippet:
                    results.append({
                        "url": href,
                        "code": code_snippet
                    })

    except Exception as e:
        print("[!] Web search error:", str(e))

    return results or [{"error": "No usable code found."}]
