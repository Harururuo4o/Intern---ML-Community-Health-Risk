
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("community_risk_screening_train.csv")
print(df.head())



# Step 3: Show the total number of rows
print("Total number of rows:", len(df))

# Step 4: Count missing phq2_score values in each region
missing_by_region = df.groupby("region")["phq2_score"].apply(
    lambda column: column.isnull().sum()
)

print("\nMissing phq2_score values by region:")
print(missing_by_region)

# Step 5: Calculate the percentage of missing values in each region
missing_percentage = df.groupby("region")["phq2_score"].apply(
    lambda column: column.isnull().mean() * 100
)

print("\nPercentage of missing phq2_score values by region:")
print(missing_percentage.round(2))