#========================================================
# BLOCK 2 - STANDARDIZE HEADERS AND REMOVE DUPLICATES
#========================================================
# GOAL:
# Ensure all datasets across cities share consistent column naming and remove duplicate rows
# before merging. This maintains schema alignment for # downstream ETL stages.
# 
# PIPELINE FLOW:
# 1. Load interim cleaned files from /data/interim/
# 2. Convert column names to lower_snake_case
# 3. Drop duplicate rows based on full record
# 4. Save standardized outputs to /data/interim/
# 5. Log results to run_log.json
# 
# NOTES:
# - Uses config-driven city list from etl_config.json
# - Outputs: standardized_[city]_listings.csv
#========================================================

import os
import pandas as pd
import numpy as np
import json
import time

# load config
with open("etl_config.json","r") as f:
    config = json.load(f)

RAW_DIR = config["data_path"]
INTERIM_DIR = config["output_path"]
LOG_FILE = os.path.join(config["log_path"], "run_log.json")
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

output_format = config["output_settings"]["format"]
output_compression = config["output_settings"]["compression"]

# convert to snake_case
def to_snake_case(name):
    return (
        name.strip()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .lower()
    )

# standardize headers and drop duplicates
def standardize_and_dedupe(df):
    # convert all column names
    df.columns = [to_snake_case(col) for col in df.columns]
    # drop duplicates
    df = df.drop_duplicates()
    return df

def run_standardize():
    print("=== 🧹 Standardize Headers and Remove Duplicated ===")
    # initizalize log entries
    block2_logs = []

    for city in config["cities"]:
        city_name = city["name"]
        input_path = os.path.join(INTERIM_DIR, f"clean_numeric_text_{city_name}.csv")
        output_path = os.path.join(INTERIM_DIR, f"standardized_{city_name}_listings.csv")

        if os.path.exists(input_path):
            df = pd.read_csv(input_path)
            std_df = standardize_and_dedupe(df)
            std_df.to_csv(output_path, index = False)

            block2_logs.append({
                "city": city_name,
                "input_file": input_path,
                "output_file": output_path,
                "rows_before": len(df),
                "rows_after": len(std_df),
                "duplicates_removed": len(df) - len(std_df),
                "columns": list(std_df.columns),
                "status": "Standardized and saved"
            })
        else:
            block2_logs.append({
                "city": city_name,
                "status": "File not found",
                "expected_file": input_path
            })

    # update run_log.json
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = {}

    logs["cleaning_stage_block2"] = block2_logs

    with open(LOG_FILE, "w", encoding=config["log_format"]["encoding"]) as f:
        json.dump(logs, f, indent= config["log_format"]["indent"], sort_keys = config["log_format"]["sort_keys"])

    print("Standardized headers and removed duplicates")
    print("=== ✅ standardize_stage.py complete ===\n")

if __name__ == "__main__":
    run_standardize()