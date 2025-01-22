from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


base_dir = Path("./").resolve()

skip_cols = [0,1]
keep_cols = [i for i in range(61) if i not in skip_cols]
df = pd.read_excel('Search_Report_2023_week_1-49.xlsx', skiprows=3, usecols=keep_cols)

filtered_df = df[df['FPA'].isin(['None'])]
filtered_df2 = filtered_df.dropna(subset='Biomarker Data')

#filtered_df2.to_excel("Search_Report_2023_week_1-49_filtered.xlsx", index=None)

plt.figure(figsize=(10,6))
sns.countplot(x='Biomarker Data', data=filtered_df2)
plt.title("Biomarker count where FPA is None")
plt.xlabel('Biomarker Data')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


def read_and_concatenate(directory):
	all_data = pd.DataFrame()

	skip_cols = [0,1]
	skip_rows = 3
	keep_cols = [i for i in range(61) if i not in skip_cols]
	
	for file_path in Path(directory).glob('*.xlsx'):
		df = pd.read_excel(file_path, skiprows=skip_rows, usecols=keep_cols)
		all_data = pd.concat([all_data, df], ignore_index=True)

	return all_data

combined_data = read_and_concatenate(base_dir)
filtered_combined_data = combined_data[combined_data['FPA'].isin(['None'])]

filtered_combined_data2 = filtered_combined_data.dropna(subset='Biomarker Data')
#filtered_combined_data2.to_excel("Week_22-46_FPA-None-Less_Combined.xlsx", index=None)


df_concat_cl = pd.read_excel('Copy of Search_Report_2023_week_1-49_filtered_edited_2.xlsx')
df_concat_cl['Biomarker Data'].value_counts()


# Create a DataFrame with counts sorted in ascending order
count_data = df_concat_cl['Test Name'].value_counts().reset_index()
count_data.columns = ['Test Name', 'Count']
count_data = count_data.sort_values(by='Count', ascending=True)


plt.figure(figsize=(10,6))
# Use the 'order' parameter to specify the order of bars on the x-axis
ax = sns.countplot(x='Test Name', data=df_concat_cl, order=count_data['Test Name'])
plt.title("Biomarker count where FPA is 'None' (2023)")
plt.xlabel('Biomarker Data')
plt.ylabel('Count')
plt.xticks(rotation=80)

# Annotate each bar with its count value
for p in ax.patches:
	ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline', fontsize=7, color='black', xytext=(0, 5),
                textcoords='offset points')

# Reduce the font size of x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), fontsize=5, ha='center')
plt.savefig("Figure_1_preliminary_FPA.pdf", bbox_inches='tight')
plt.show()
