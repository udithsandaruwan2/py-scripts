import pandas as pd

# Read Excel files
main_df = pd.read_excel('main.xls')
update_df = pd.read_excel('codes.xlsx')

# Clean column names
main_df.columns = main_df.columns.map(str).str.strip()
update_df.columns = update_df.columns.map(str).str.strip()

# Debug prints
print("Main Columns:", main_df.columns.tolist())
print("Update Columns:", update_df.columns.tolist())

# Validate 'Code' column
if 'code' not in main_df.columns:
    raise KeyError("❌ 'Code' column not found in main.xlsx.")
if 'code' not in update_df.columns:
    raise KeyError("❌ 'Code' column not found in codes.xlsx.")

# Select only relevant columns from update_df
columns_to_add = ['code', '2020', '2025']
missing_cols = [col for col in columns_to_add if col not in update_df.columns]
if missing_cols:
    raise KeyError(f"❌ Missing columns in codes.xlsx: {missing_cols}")

update_df = update_df[columns_to_add]

# Merge only 2020 and 2025 columns into main_df
merged_df = pd.merge(main_df, update_df, on='code', how='left')

# Save the result
merged_df.to_excel('updated_main.xlsx', index=False)
print("✅ Columns '2020' and '2025' added. File saved as 'updated_main.xlsx'")
