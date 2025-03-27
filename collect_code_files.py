import os

# Folder to start collecting from
BASE_DIR = "D:/Edthra_APIs"
OUTPUT_FILE = "D:/Edthra_APIs/edithra_all_code_dump.txt"

# File extensions to include
INCLUDE_EXT = [".py"]

def collect_codes():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        for folder, _, files in os.walk(BASE_DIR):
            for filename in files:
                if any(filename.endswith(ext) for ext in INCLUDE_EXT):
                    filepath = os.path.join(folder, filename)
                    outfile.write(f"\n\n\n# === {filepath} ===\n")
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            outfile.write(f.read())
                    except Exception as e:
                        outfile.write(f"\n# Error reading {filepath}: {e}\n")

    print(f"[✓] All code collected to: {OUTPUT_FILE}")

if __name__ == "__main__":
    collect_codes()
