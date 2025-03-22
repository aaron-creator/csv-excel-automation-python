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
        <h1>CSV Excel Automation App</h1>
        <div className="">
            <h2>Sales Data Filter</h2>

            <label>Start Date:</label>
            <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
            <br />
            <label>End Date:</label>
            <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
            <br />
            <button className="button" onClick={handleFilter}>Download Excel Report</button>
            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
      </div>
    </>
  )
}

export default App
