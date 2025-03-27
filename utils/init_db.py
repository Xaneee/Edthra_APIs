import sqlite3
import os

DB_PATH = "memory.db"

def init_memory_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            tags TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Memory table initialized successfully.")

if __name__ == "__main__":
    init_memory_table()
