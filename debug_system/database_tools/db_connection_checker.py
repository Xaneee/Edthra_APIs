import sqlite3

DATABASE_PATH = "memory.db"

def check_db_connection():
    print("🔎 Checking Database Connection...")
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if tables:
            print("[✓] Database Connected Successfully ✅")
            print(f"Tables Found: {tables}")
        else:
            print("[⚠️] Connected but No Tables Found.")
    except Exception as e:
        print(f"[✗] Database Connection Failed: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_db_connection()
