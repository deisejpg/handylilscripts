import pandas as pd

# Define the data (shortened for demonstration)
data = [
    "IIB T3NxMx", "IIIA T1N2M0", "IIA T2N0M0", "I", "IV T2N3aM1",
    "UNK TXNXM0", "IIIC T3N3cM0", "IA T1bN0M0", "0is TisN0MX",
    "IIA T1cN1aM0", "IIIB T4bN2aM0", "IV T4N1M1", "II T3N0M0",
    "IIIB T4N3M0", "IV TXNXM1", "IIIA T3N1M0", "IVB T4N2bM1b"
]

# Define classification criteria
low_shed = ["Stage 0", "Stage I", "Stage IA", "Stage IB", "Stage IS", "Stage IIA"]
high_shed = ["Stage IIIB", "Stage IIIC", "Stage IVA", "Stage IVB", "Stage IVC", "Stage IIIA (aggressive)"]
unknown = ["UNK", "TXNXM0", "NA"]

# Classification function
def classify_stage(entry):
    if any(stage in entry for stage in low_shed):
        return "Low-Shed"
    elif any(stage in entry for stage in high_shed):
        return "High-Shed"
    elif any(stage in entry for stage in unknown) or "N/A" in entry:
        return "Unknown/Not Determined"
    else:
        return "Unknown/Not Determined"

# Apply classification
classified_data = [{"Original_Entry": entry, "Classification": classify_stage(entry)} for entry in data]

# Convert to DataFrame
df = pd.DataFrame(classified_data)

# Save to CSV
output_path = "/mnt/data/cancer_staging_classification.csv"
df.to_csv(output_path, index=False)

# Display the DataFrame for review
import ace_tools as tools; tools.display_dataframe_to_user(name="Cancer Staging Classification", dataframe=df)
