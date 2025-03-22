import pandas as pd
from flask import Flask, send_file, request, jsonify
import os

# Create a flask app
app = Flask(__name__)

# Enable CORS for React frontend
from flask_cors import CORS
CORS(app)

# Load CSV file (ensure it's in the same folder as app.py)
CSV_FILE = "sales_data.csv"

#define a route for homepage
@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app