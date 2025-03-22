import pandas as pd

# Read the CSV file
df = pd.read_csv("sales_data.csv")

print(f"data from CSV files here \n{df}")

# Add a new column for Total Sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Sort by highest sales
df = df.sort_values(by="Total Sales",ascending=False)

# Sort by highest sales
df.to_excel("Sales_Report.xlsx",index=False)
print("Excel report generated successfully!")

