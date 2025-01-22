import pandas as pd

df = pd.read_excel('Mutation test results.xlsx', skiprows = 1)

filtered_df = df[df['Result Inference Type Name'] == "Self"]

df2 = pd.read_excel("inventory_sample list.xlsx")

merged_df = pd.merge(df2, filtered_df[['Case ID', 'Com ID']], on='Case ID', how='left')

cleaned_df = merged_df.drop_duplicates(subset='Com ID', keep='first')

cleaned_df.to_excel('inventory_sample_list_withScreenedSamples.xlsx', index=False)
