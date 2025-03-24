import pandas as pd
from flask import Flask, send_file, request, jsonify
import os
from flask_cors import CORS
import io

# Create a Flask app
app = Flask(__name__)

# Enable CORS for React frontend
CORS(app)

# Load CSV file (ensure it's in the same folder as app.py)
CSV_FILE = "sales_data.csv"

PORT = int(os.getenv("PORT", 5000))  # Default to 5000
SECRET_KEY = os.getenv("SECRET_KEY", "55f8cd7ef438f22e20295220419a9a3d81136194e3e88c92")

app.config["SECRET_KEY"] = SECRET_KEY


# Define a route for filtering sales data
@app.route('/filter', methods=['POST'])
def filter_sales():
    try:
        data = request.json
        print("Received data:", data)

        if not data:  # Check if None or empty
            print("❌ No data received")
            return jsonify({"error": "No data received"}), 400

        start_date = pd.to_datetime(data.get("start_date"))
        end_date = pd.to_datetime(data.get("end_date"))
        print(f"📅 Start Date: {start_date}, End Date: {end_date}")

        # Read CSV for data frame
        df = pd.read_csv(CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"])
        print(f"📊 Loaded DataFrame: {df.shape[0]} rows")

        # Filter by date
        filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
        print(f"✅ Filtered DataFrame: {filtered_df.shape[0]} rows")
        filtered_df["Total Sales"] = filtered_df["Quantity"] * filtered_df["Price"]

        if filtered_df.empty:
            print("❌ No matching data found")
            return jsonify({"error": "No data found for selected dates"}), 400

        # Generate Excel file in memory
        try:
            print("📂 Generating Excel file...")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                filtered_df.to_excel(writer, index=False)

            output.seek(0)  # Reset pointer before sending
            print("📂 Excel file ready to send")

            return send_file(
                output,
                download_name="filtered_sales_report.xlsx",
                as_attachment=True,
                mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            print(f"❌ Error generating Excel file: {e}")
            return jsonify({"error": str(e)}), 500

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)  # Run the Flask app
