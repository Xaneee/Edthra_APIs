import sqlite3

DATABASE_PATH = "memory.db"

def check_db_integrity():
    print("🔎 Running Database Integrity Check...")
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA integrity_check;")
        result = cursor.fetchone()

        if result and result[0] == "ok":
            print("[✓] Database Integrity Verified ✅")
        else:
            print(f"[✗] Integrity Check Failed: {result}")
    except Exception as e:
        print(f"[✗] Database Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_db_integrity()
