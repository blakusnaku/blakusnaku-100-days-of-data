#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: Auto — Python ACTION
# Task: Full Modular Automation Pipeline Orchestrator
# Phase: Full ETL (Cleaning → Harmonization → Transformation → KPIs → Export)
# Dataset: InsideAirbnb — Multi-City STR Pipeline
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/modular_automation_pipeline.py
#===========================================================
#
# 🎯 GOAL:
# Execute the entire multi-stage STR ETL pipeline in the correct order,
# using modular stage runner scripts and config-driven logic.
# 
# 🔁 PIPELINE FLOW:
# 1. Stage 1 — City Cleaning
# 2. Stage 2 — Harmonization
# 3. Stage 3 — Transformation (BI-prep)
# 4. Stage 4 — KPI Modeling
# 5. Stage 5 — Export Master Tables for Power BI
# 
# 📘 NOTES:
# - This script should never contain ETL logic.
# - It only calls stage runner modules.
# - All logic lives in individual stage scripts.
# - This design mirrors Airflow/Dagster/dbt orchestrator patterns.
#
#===========================================================

from scripts._01_run_cleaning import run_city_cleaning
from scripts._02_run_harmonization import run_harmonization
from scripts._03_run_transformation import run_transformation
from scripts._04_run_kpi_modeling import run_kpi_modeling

# Future stage imports (added as you build them)
# from scripts._03_run_transformation import run_transformation
# from scripts._04_run_kpi_modeling import run_kpi_modeling
# from scripts._05_run_export_master import run_export_master


def run_full_pipeline(config_path="etl_config.json"):
    """Run all ETL stages in sequence."""

    print("\n🚀 Starting FULL STR ETL Pipeline...\n")

    # ---------------------------
    # STAGE 1 — CLEANING
    # ---------------------------
    print("🔹 Stage 1: Cleaning")
    run_city_cleaning(config_path=config_path)

    # ---------------------------
    # STAGE 2 — HARMONIZATION
    # ---------------------------
    print("🔹 Stage 2: Harmonization")
    run_harmonization(config_path=config_path)

    # ---------------------------
    # STAGE 3 — TRANSFORMATION 
    # ---------------------------
    print("🔹 Stage 3: Transformation")
    run_transformation(config_path=config_path)

    # ---------------------------
    # STAGE 4 — KPI MODELING
    # ---------------------------
    print("🔹 Stage 4: KPI Modeling")
    run_kpi_modeling(config_path=config_path)

    # ---------------------------
    # STAGE 5 — EXPORT FOR POWER BI
    # (Coming later)
    # ---------------------------
    # print("🔹 Stage 5: Exporting BI Tables")
    # run_export_master(config_path=config_path)

    print("\n🎉 FULL STR ETL PIPELINE COMPLETE!\n")


if __name__ == "__main__":
    run_full_pipeline()
