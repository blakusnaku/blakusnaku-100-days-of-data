
import sqlite3
import json

CONFIG_PATH = "etl_config.json"

#load config
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

DB_PATH = config['db_path']
SCHEMA_FILE = "scripts/str_schema.sql"

# call str_schema.sql
def run_load_schema_sql():

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