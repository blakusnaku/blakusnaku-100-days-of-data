#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Project: US STR Pipeline
# Process: automation_pipeline.py
# Phase: Full ETL Orchestrator
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#===========================================================

from scripts.schema_validation import run_schema_validation

from scripts.clean_numeric_stage import run_clean_numeric
from scripts.standardize_stage import run_standardize
from scripts.merge_listings_calendar import run_merge_listings_calendar 
from scripts.load_datasets import run_load
from scripts.harmonize_schemas import run_harmonize
from scripts.merge_stage import run_merge

def main():
    print(" Starting US STR Data Pipeline\n")

    #step 1: schema validation
    run_schema_validation()

    #step 2: clean numeric
    run_clean_numeric()
    
    #step 3: standardize
    run_standardize()

    #step 4: merge listings + calendar
    run_merge_listings_calendar()

    #step 5: load standardized listings
    run_load()

    #step 6: harmonize schemas and add city columns
    run_harmonize()

    #step 7: run merge
    run_merge()

if __name__ == "__main__":
    main()