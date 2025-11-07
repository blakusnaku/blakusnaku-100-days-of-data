#========================================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------------------
# Day: 38 
# Date: 2025-11-05
# Process: metrics_utils.py
# Task: Reusable KPI calculation functions
# Phase: Data Acquistition - KPI Transformation
# Tools: Python (pandas, numpy)
# Author: JP Malit
#========================================================================

import pandas as pd
import numpy as np

# === Core KPI Functions === #

def compute_adr(df: pd.DataFrame) -> pd.Series:
    # Average Daily Rate: derived directly from price column.
    return df["price"]

def compute_occupancy(df: pd.DataFrame) -> pd.Series:
    # Occupancy percentage: (365 - available_days)/365 *100.
    if "availability_365" in df.columns:
        return ((365 - df["availability_365"])/365*100).clip(0,100)
    elif "occupancy_pct" in df.columns:
        return df["occupancy_pct"].clip(0,100)
    else:
        raise KeyError("No availability_365 or occupancy_pct column found")
    
def compute_revpar(df: pd.DataFrame) -> pd.Series:
    # Revenue per Available Room: ADR x (Occupancy/100).
    adr = compute_adr(df)
    occ = compute_occupancy(df)
    return adr * (occ/100)

def compute_los(df: pd.DataFrame) -> pd.Series:
    #Length of Stay proxy: use minimum_nights or fallback to median.
    if "minimum_nights" in df.columns:
        return df["minimum_nights"].fillna(df["minimum_nights"].median())
    return pd.Series(np.nan, index=df.index)

# === aggregation helper === #

def summarize_city_kpis(df: pd.DataFrame) -> pd.DataFrame:
    #Aggregtate key metrics per city_display.
    summary = (
        df.groupby("city_display")
        .agg(
            listings=("listing_id","count"),
            avg_adr=("adr","mean"),
            avg_occupancy=("occupancy_pct","mean"),
            avg_revpar=("revpar","mean"),
            avg_los=("los","mean"),
        )
        .reset_index()
        .round(2)
    )
    return summary