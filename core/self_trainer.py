from core.web_crawler import crawl_search
from core.knowledge_extractor import extract_code_from_url
from utils.memory_utils import save_memory

def learn_topic(topic: str):
    links = crawl_search(topic)
    for url in links:
        code_blocks = extract_code_from_url(url)
        for code in code_blocks:
            save_memory(f"Learned: {topic}", code, tags=f"web, {topic}")
    return f"[✓] Learned from {len(links)} sources about '{topic}'."
