
import sqlite3

# call str_schema.sql
def run_load_schema_sql():
    DB_PATH = "data/str_market.db"
    SCHEMA_FILE = "scripts/str_schema.sql"

    # Connect and execute
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cur.executescript(schema_sql)
    conn.commit()
    conn.close()

    print("✅ Database schema initialized successfully!")

if __name__ == "__main__":
    run_load_schema_sql()