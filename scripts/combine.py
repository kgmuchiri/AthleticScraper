import os
import pandas as pd

# Set the folder containing all your combined discipline files
combined_dir = "combined"  # Adjust if located elsewhere

# List all CSV files
csv_files = [f for f in os.listdir(combined_dir) if f.endswith(".csv")]

# Load and concatenate
all_dataframes = []
for file in csv_files:
    df = pd.read_csv(os.path.join(combined_dir, file))
    df["source_file"] = file  # Optional: track original file
    all_dataframes.append(df)

# Combine into a single DataFrame
combined_df = pd.concat(all_dataframes, ignore_index=True)

# Save to a new CSV
combined_df.to_csv("all_disciplines_combined.csv", index=False)

print("✅ Combined CSV saved as 'all_disciplines_combined.csv'")
