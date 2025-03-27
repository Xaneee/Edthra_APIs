import sqlite3
import os

DB_PATH = "data/edithra.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            tags TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            message TEXT,
            reason TEXT
        )
    ''')
    conn.commit()
    conn.close()
