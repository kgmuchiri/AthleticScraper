import numpy as np
import pandas as pd
import os


df = pd.read_csv('datasets/all_disciplines_combined.csv')
df2 = pd.read_csv('datasets/all_disciplines_combined.csv')

df=df.drop("source_file",axis=1)
df2=df2.drop("source_file",axis=1)
df2=df2.drop("DOB",axis=1)
df2=df2.drop("age_at_event",axis=1)

df = df[df["Type"] != "relays"]
df2 = df2[df2["Type"] == "relays"]

df.to_csv("datasets/individual_events.csv", index=False)
df2.to_csv("datasets/relay_events.csv", index=False)


# Make sure output directory exists
output_dir = "../datasets/split_by_type"
os.makedirs(output_dir, exist_ok=True)

# Group by 'type' and save each group as a separate CSV
for event_type, df_group in df.groupby("Type"):
    filename = f"{event_type}.csv"
    filepath = os.path.join(output_dir, filename)
    df_group.to_csv(filepath, index=False)
    print(f"✅ Saved: {filepath}")
