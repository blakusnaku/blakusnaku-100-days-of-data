import pandas as pd
df = pd.read_parquet("data/interim/validated_master_v2.parquet")
print(df["city_display"].value_counts())