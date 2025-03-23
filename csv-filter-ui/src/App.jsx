import React, { useState } from "react";
import axios from "axios";
import './App.css'

function App() {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [error, setError] = useState("");

  const handleFilter = async () => {
    try {
      const response = await axios.post("https://sales-data-filter-app.onrender.com:5000/filter", {
        start_date: startDate,
        end_date: endDate,
      }, { responseType: "blob" });

      // Create a link to download the file
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "filtered_sales_report.xlsx");
      document.body.appendChild(link);
      link.click();
    } catch (err) {
      setError("Error generating the report. Try again.");
    }
  };

  return (
    <>
      <div className="@container">
        <div className="max-w-4xl mx-auto p-6 bg-white shadow-lg rounded-lg">
            <h2 className="text-xl font-bold mb-4">Sales Data Filter</h2>

            <label>Start Date:</label>
            <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
            <br />
            <label>End Date:</label>
            <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
            <br />

            <button className="mt-4 px-6 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
                onClick={handleFilter} // Replace with actual download function
              >
                Download Excel Report
            </button>
        </div>
      </div>
    </>
  )
}

export default App
