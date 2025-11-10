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

from scripts.validate_data_completeness import run_data_quality_check 
from scripts.validate_missing_outliers import run_missing_outlier_treatment
from scripts.validate_numeric_consistency import run_numeric_validation

from scripts.calculate_kpis  import run_calculate_kpis
from scripts.generate_kpi_summary import run_kpi_summary

from scripts.import_to_sqlite import run_import_to_sqlite
from scripts.verify_sql_import import run_verify_import

from scripts.export_bi_dataset import run_export_bi_dataset
from scripts.inspect_str_market_data import run_inspect_str_market_data
from scripts.standardize_numeric_fields import run_standardize_numeric_fields
from scripts.handle_missing_outliers import run_handle_missing_outliers

from scripts.extract_amenity_keywords import run_extract_amenity_keywords
from scripts.analyz_amenity_impact import run_analyze_amenity_impact
from scripts.visualize_amenity_impact import run_visualize_amenity_impact
def main():
    print("=== 🚀 Starting US STR Data Pipeline ===")

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

    #step 8: check data qulity
    run_data_quality_check()

    #step 9: check for missing data and outliers
    run_missing_outlier_treatment()

    #step 10: validate numeric consistency
    run_numeric_validation()

    #step 11: calculate kpis
    run_calculate_kpis()

    #step 12: generate kpi summary
    run_kpi_summary()

    #step 13: import to sqlite database
    run_import_to_sqlite()
    
    #step 14: verify_sql_import
    run_verify_import()
    
    #step 15: export bi dataset
    run_export_bi_dataset()
    
    #step 16: inspect str market data
    run_inspect_str_market_data()

    #step 17: standardize numeric fields
    run_standardize_numeric_fields()

    #step 18: handle missing values and detect outliers
    run_handle_missing_outliers()

    #step 19: extract amenity keywords
    run_extract_amenity_keywords()
    
    #step 20: analyze amenity impact
    run_analyze_amenity_impact()

    #step 21: visualize amenity impact
    run_visualize_amenity_impact()
    
if __name__ == "__main__":
    main()