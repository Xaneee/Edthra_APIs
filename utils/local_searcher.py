import os

def local_doc_search(query):
    base_dir = "local_knowledge"
    results = []

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        results.append({
                            "file": file,
                            "match": content[:200] + "..."
                        })

    return results or [{"message": "No match found in local docs."}]
