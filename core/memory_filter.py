# core/memory_filter.py

from database import get_db

def refine_memory(threshold=5):
    conn = get_db()
    c = conn.cursor()

    # Target low-score or short entries for deletion
    c.execute("""
        SELECT id, title, content, tags FROM memories 
        WHERE LENGTH(content) < 50 
        OR tags LIKE '%discard%' 
        LIMIT ?
    """, (threshold,))
    
    deletable = c.fetchall()

    deleted_ids = []
    for mem in deletable:
        mem_id = mem[0]
        c.execute("DELETE FROM memories WHERE id = ?", (mem_id,))
        deleted_ids.append(mem_id)

    conn.commit()
    return {
        "status": "refined",
        "deleted_entries": deleted_ids or ["None marked as noise."]
    }
