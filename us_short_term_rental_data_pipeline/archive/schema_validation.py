#===========================================================
# PROJECT: US STR Pipeline - (Day34) Block 3 Schema Validation
#-----------------------------------------------------------
# Date: 2025-11-01
# Authour: JP Malit
# Goal: Inspect schema structure and key fields for each city
#===========================================================

import os
import json
import pandas as pd
from datetime import datetime

# load configuration
with open('etl_config.json') as f:
    config = json.load(f)

log_path = os.path.join(config['log_path'], "run_log.json")

# initialize run log entry
run_entry = {
    "timestamp": datetime.now().isoformat(),
    "task": "schema_validation",
    "cities": {},
    "status": "in_progress"
}

# helper: safe file loader
def load_csv_safe(path):
    try:
        df = pd.read_csv(path,compression="infer")
        return df, "success"
    except Exception as e:
        print(f"X Error loading {path}:{e}")
        return None, str(e)

# main inspection loop

def run_schema_validation():
    print("=== 🧩 Running Schema Validation ===")
    for city in config['cities']:
        city_name = city['name']
        city_display = city['display_name']
        print(f"\n🏦 Inspecting {city_display}...")

        city_result = {}
        for file in city["files"]:
            file_path = os.path.join(config['data_path'],city_name,file)
            df, status = load_csv_safe(file_path)

            if df is not None:
                info = {
                    "rows": int(df.shape[0]),
                    "columns": int(df.shape[1]),
                    "column_names": list(df.columns[:10]),
                    "status": status
                }

                # detect key columns if present
                if "id" in df.columns:
                    info["unique_id"] = df["id"].nunique()
                elif "listing_id" in df.columns:
                    info["unique_id"] = df["listing_id"].nunique()

                city_result[file] = info

                # basic dtype sample
                print(f" {file}: {df.shape[0]} rows, {df.shape[1]} cols")

            else:
                city_result[file] = {"status": status}
                
        run_entry["cities"][city_name] = city_result

    # finalize log
    run_entry["status"] = "completed"
    os.makedirs(config['log_path'], exist_ok=True)

    # append the run_log.json
    if os.path.exists(log_path):
        with open(log_path) as f:
            log_data = json.load(f)
    else:
        log_data = {"runs":[]}

    log_data["runs"].append(run_entry)

    with open(log_path,"w") as f:
        json.dump(log_data,f,indent=2)

    print("\n✅ Schema inspection complete! Results logged to run_log.json")
    print("== ✅ schema_validation.py complete ==\n")

if __name__ == "__main__":
    run_schema_validation()