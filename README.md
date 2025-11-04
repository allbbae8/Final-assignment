# Final-assignment

Data Analysis of Hotels in Vienna

This is Data Analysis 1 final assignment. It uses Python and Stata to clean, prepare, and analyze a dataset of hotels in Vienna.  
The goal is to demonstrate key data analysis steps, starting from fixing data quality issues to creating visualizations, like graphs.

Project Structure:

DA-final_assignment/
│
├── data/
│ └── hotels-vienna.csv # Original dataset
│
├── vienna_hotels_clean.csv # Cleaned and prepared dataset
│
├── main.py # Main Python script (contains all tasks)
│
└── README.md # Project description and guide

This covers multiple small tasks that show data analysis skills. In order of the file: 

Task 3: Lists and Dictionaries
1. Demonstrates how to use Python lists and dictionaries.
2. Filters data using a list of neighborhoods.
3. Compares each hotel’s price with a type’s average using a dictionary.

Task 5: Fixing Data Quality
1. Identifies numeric and categorical columns.
2. Converts incorrect data types.
3. Fills missing numeric values with the mean.
4. Fills missing text values with `"Unknown"`.

Task 6: Data Preparation
1. Filters observations: keeps only hotels in Vienna with price > 50 and rating > 4.
2. Filters variables: selects only relevant columns for analysis.
3. Creates new variables: 
  - `price_per_star` (price divided by number of stars)  
  - `log_price` (logarithm of price)  
  - `near_center` (True if distance < 2 km)

Task 7: Save Clean Data
Exports the cleaned and filtered dataset into `vienna_hotels_clean.csv`.

Task 8: Summary Statistics
1. Uses `pandas.describe()` to show mean, min, max, std, etc.
2. Provides an overview of numeric variables.

Task 9: Visualization
1. Calculates average hotel price by accommodation type.
2. Creates a simple bar chart using `matplotlib`.

  
