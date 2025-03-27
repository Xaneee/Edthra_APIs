from urllib.parse import unquote, urlparse

def clean_url(raw):
    if "duckduckgo.com/l/" in raw:
        raw = raw.split("uddg=")[-1]
    return unquote(raw)
