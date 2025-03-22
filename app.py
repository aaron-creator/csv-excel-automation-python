import pandas as pd
from flask import Flask, send_file, request, jsonify
import os
from flask_cors import CORS

# Create a flask app
app = Flask(__name__)

# Enable CORS for React frontend
CORS(app)

# Load CSV file (ensure it's in the same folder as app.py)
CSV_FILE = "sales_data.csv"

#define a route for homepage
@app.route('/filter', methods=['POST'])
def filter_sales():
    try:
        data = request.json
        print("Received data:", data)
        print("in try block")
        if data is None or not data:  # Check if None or empty
            print("In if block")
            return jsonify({"error": "No data received"}), 400
        else:
            print("In else block")
            print(f"Data received{data}")
            start_Date = pd.to_datetime(data.get("start_date"))
            end_Date = pd.to_datetime(data.get("end_date"))
            print(f"Start Date {start_Date} and End Date {end_Date}")
            #Read CSV for data frame as df
            df = pd.read_csv(CSV_FILE)
            df["Date"] = pd.to_datetime(df["Date"])
            print(f"df value {df}")
            # Filter by date
            filtered_df = df[(df["Date"] >= start_Date) & (df["Date"] <= end_Date)]

            # Adding a new column Total Sales
            filtered_df["Total Sales"] = filtered_df["Quantity"] * filtered_df["Price"]

            # Save filtered data as Excel
            output_file = "filtered_sales_report.xlsx"
            filtered_df.to_excel(output_file, index=False)
            print("Excel report generated successfully!")
            return send_file(output_file, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app