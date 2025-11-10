#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 42
# Date: 2025-11-09
# Process: visualize_amenity_impact.py
# Block: 3 - Visualize amenity frequency vs ADR
# Phase: Data Analysis - Feature Exploration
# Dataset: amenity_impact_summary.csv
# Tool: Python (pandas, matplotlib)
# Author: JP Malit
#===========================================================

import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
INPUT_FILE = os.path.join(INTERIM_DIR, "amenity_impact_summary.csv")

def run_visualize_amenity_impact():
    print("=== 📊 Visualizing Amenity Frequency vs ADR ===")

    df = pd.read_csv(INPUT_FILE)

    top_amenities = df.sort_values("listings_with", ascending=False).head(15)

    plt.figure(figsize=(10,6))
    plt.barh(
        top_amenities["amenity"],
        top_amenities["avg_adr"],
        color="orange",
        alpha=0.8
    )

    plt.xlabel("Average Daily Rate (ADR)")
    plt.ylabel("Amenity")
    plt.title("Amenity Frequency vs Average ADR — STR Market")
    plt.gca().invert_yaxis()  # highest ADR on top
    plt.tight_layout()

    output_path = os.path.join(INTERIM_DIR, "amenity_vs_adr_chart.png")
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"💾 Saved visualization ➡ {output_path}")
    print("=== ✅ visualize_amenity_impact.py complete ===\n")


if __name__ == "__main__":
    run_visualize_amenity_impact()
