import sqlite3

DATABASE_PATH = "memory.db"

def check_data_existence(table_name):
    print(f"🔎 Checking Data in Table: {table_name}")
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]

        if count > 0:
            print(f"[✓] Data Found: {count} records in '{table_name}' ✅")
        else:
            print(f"[⚠️] No Data Found in '{table_name}'")
    except Exception as e:
        print(f"[✗] Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    table_name = input("Enter Table Name: ")
    check_data_existence(table_name)
