
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("/Users/allbae/Desktop/DA final_assignment/data/hotels-vienna.csv")

# Check the first few rows
print(df.head())

# Task 8
# Summary statistics for all numeric columns
summary = df.describe()

print(summary)

# Task 9: Graph
# 2. Calculate average price by accommodation type
avg_price = df.groupby("accommodation_type")["price"].mean()

# 3. Making a bar chart
avg_price.plot(kind="bar")

# 4. Add labels and the title
plt.title("Average Price by Accommodation Type")
plt.xlabel("Accommodation Type")
plt.ylabel("Average Price (€)")

# 5. Display the chart
plt.show()


# Task 5 and using for loop
# Find which columns are numeric and which are text (categorical)
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

print("Numeric columns:", list(numeric_cols))
print("Categorical columns:", list(categorical_cols))

# Convert all numeric columns to numbers
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="ignore")

# Fill missing values:
# fill numeric values with the column mean
# fill missing text values with "Unknown"
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

for col in categorical_cols:
    df[col].fillna("Unknown", inplace=True)

# Check the result
print(df.info())

# Task 6: sample analysis

# a)Filter observations: keep only hotels in Vienna with price above 50 and rating above 4
filtered_df = df[(df["city"] == "Vienna") & (df["price"] > 50) & (df["rating"] > 4)]

print("After filtering observations:", filtered_df.shape)

# b) Filter variables: keep only useful columns for further analysis
selected_columns = [
    "city", 
    "neighbourhood", 
    "price", 
    "stars", 
    "rating", 
    "distance", 
    "accommodation_type"
]
filtered_df = filtered_df[selected_columns]

print("After filtering variables:", filtered_df.columns)

# c)Create new variables (transformations)
filtered_df["price_per_star"] = filtered_df["price"] / filtered_df["stars"]
filtered_df["log_price"] = filtered_df["price"].apply(lambda x: np.log(x) if x > 0 else 0)
filtered_df["near_center"] = filtered_df["distance"] < 2

# Just checking
print(filtered_df.head())

# Task 7: Save dataset to a new file
filtered_df.to_csv("vienna_hotels_clean.csv", index=False)

# Task 3: lists and dictionaries
# Create a list of neighborhoods to keep
preferred_neighbourhoods = ["Innere Stadt", "Alsergrund", "Leopoldstadt"]

# Filter to include only those neighborhoods
filtered_df = df[df["neighbourhood"].isin(preferred_neighbourhoods)]

print("Hotels in selected neighborhoods:")
print(filtered_df[["neighbourhood", "price", "rating"]].head())

# Using a dictionary with average price by accommodation type
avg_price_by_type = {
    "Hotel": 90,
    "Apartment": 70,
    "Hostel": 40
}

# Create a new column showing if price is above average 
filtered_df["above_avg_price"] = filtered_df.apply(
    lambda row: row["price"] > avg_price_by_type.get(row["accommodation_type"], 0), axis=1
)

print("\nNew variable created using dictionary:")
print(filtered_df[["accommodation_type", "price", "above_avg_price"]].head())


