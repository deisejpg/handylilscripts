import pandas as pd

''' 
    This is handy to extract Serology test results that are stored as values   
    of a column and separated by a comma, to add the tests to separate columns.

'''

df = pd.read_excel("filename.xlsx", skiprows=10)
filtered_df = df.dropna(subset="Clinical Test Results")

filtered_df['Clinical Test Results'] = df['Clinical Test Results'].str.split(', ')
filtered_df = filtered_df.explode('Clinical Test Results').reset_index(drop=True)

def extract_units(value):
    parts = value.split(': ')
    return  parts[0] if len(parts) > 1 else None
    
filtered_df['test unit'] = filtered_df['Clinical Test Results'].apply(extract_units)
filtered_df['Clinical Test Results'] = df['Clinical Test Results'].str.split('(').str[0].str.strip()
filtered_df.to_excel('Test2.xlsx', index=False)


filtered_df2 = df.dropna(subset="ER")
filtered_df2 = filtered_df2.explode('ER').reset_index(drop=True)
filtered_df2.to_excel('Test4_er.xlsx', index=False)

filtered_df3 = df.dropna(subset="PR")
filtered_df3 = filtered_df3.explode('PR').reset_index(drop=True)
filtered_df3.to_excel('Test5_pr.xlsx', index=False)

filtered_df4 = df.dropna(subset="Hercep Test")
filtered_df4 = filtered_df4.explode('Hercep Test').reset_index(drop=True)
filtered_df4.to_excel('Test6_hercep.xlsx', index=False)
filtered_df4.to_excel('Test6_hercep.xlsx', index=False)

filtered_df5 = df.dropna(subset="Serology")
filtered_df5['Serology'] = filtered_df5['Serology'].str.split('\) ')
filtered_df5 = filtered_df5.explode('Serology').reset_index(drop=True)
filtered_df5['Serology'] = filtered_df5['Serology'].str.split('\(Tested:Yes,Result:')
filtered_df5.to_excel('Test7_serology.xlsx', index=False)
