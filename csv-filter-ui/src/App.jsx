import React, { useState } from "react";
import axios from "axios";
import './App.css'

function App() {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [error, setError] = useState("");

  const handleFilter = async () => {
    if (!startDate || !endDate) {
        setError("Please select both start and end dates.");
        return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000/filter", {
        start_date: startDate,
        end_date: endDate,
      }, { responseType: "blob" });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "filtered_sales_report.xlsx");
      document.body.appendChild(link);
      link.click();

      // Clean up
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
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
            <button
              className="px-6 py-3 text-white bg-blue-500 rounded-lg shadow-lg hover:bg-blue-600"
              onClick={handleFilter} // Remove the arrow function and directly call handleFilter
            >
              Download Excel Report
            </button>

            {error && <p style={{ color: "red" }}>{error}</p>}

        </div>
      </div>
    </>
  )
}

export default App
