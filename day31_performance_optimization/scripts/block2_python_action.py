###########################################
# PROJECT METADATA
#------------------------------------------
# Day: 31
# Date: 2025-10-29
# Block: 2 - PYTHON ACTION
# Task: Benchmark pandas Load speed for calnedar.csv
# Phase: STR Dtaset - STR Pipeline Flow
# Dataset: calendar.csv
# Tool: Python (pandas)
# Author: JP Malit
# Repo: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
#--------------------------------------------
# GOAL:
#   measure and compare CSV load times using different 
#   pandas.read_csv() techniques:
#       - default load
#       - dtype optimization
#       - usecols filtering
#       - parse_dates conversion
#
# PIPELINE FLOW:
#   1. measure baseling load time with default read_csv
#   2. apply dtype hints and usecols to improve parsing efficiency
#   3. compare results using %%time or timeit
#   4. record timing differences for BLock 4 summary
#
# NOTES:
#   - run this in Jupyter or IPythong to use %%time
#   - for console runs, use time.time() before/after each load
#   - use memory_usage(deep=True) to assess memory footprint
#
#---------------------------------------------

import pandas as pd
import time

# step 1 - baseline load
start = time.time()
df_base = pd.read_csv(r'data/calendar.csv')
end = time.time()
print(f"Baseline load time: {end - start:.4f} seconds, shape: {df_base.shape}")

# step 2 - promized load (specify dtypes and parse dates)
dtype_map = {
    "listing_id"    : "int32",
    "price"         : "float32",
    "avilable"      : "bool"
}
start = time.time()
df_opt = pd.read_csv(
    r'data/calendar.csv',
    dtype = dtype_map,
    parse_dates = ['date'],
    usecols=['listing_id','date','price','available']
)
end = time.time()
print(f"Optimized load time: {end - start:.4f} seconds, shape: {df_opt.shape}")

# step 3 - compare memory usage
print("\nMemory Usage Comparison (MB):")
print(df_base.memory_usage(deep=True).sum() / 1_000_000, " - baseline")
print(df_opt.memory_usage(deep=True).sum() / 1_000_000, " - optimized")

# sTEP 4 — Export optimized dataset for Power BI test
df_opt.to_csv(r"data/calendar_optimized.csv", index=False)
print("✅ Exported optimized dataset → data/calendar_optimized.csv")