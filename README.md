# Sales Data Filtering App

## 📌 Project Overview

This application allows users to filter sales data based on a date range and download the results as an Excel report. It consists of a **React frontend** and a **Flask backend** for seamless interaction.

## 🛠 Tech Stack

- **Frontend**: React.js, Vite, Tailwind CSS
- **Backend**: Flask, Pandas
- **Database/Storage**: CSV Files
- **Other**: Axios, CORS

---

## 🚀 Features

- Upload and filter sales data
- Generate an Excel report
- Simple and user-friendly UI
- API integration between Flask & React

---

## 📦 Installation

### **Backend Setup (Flask)**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sales-filter-app.git
   cd sales-filter-app/backend
   ```
2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Flask server**
   ```bash
   python app.py
   ```
   The server will run on `http://127.0.0.1:5000`.

---

### **Frontend Setup (React)**

1. **Navigate to the frontend folder**
   ```bash
   cd ../frontend
   ```
2. **Install dependencies**
   ```bash
   npm install
   ```
3. **Start the React app**
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`.

---

## 🔗 API Endpoints

### `POST /filter_sales`

- **Description**: Filters sales data based on the provided date range and returns an Excel file.
- **Request Format (JSON)**:
  ```json
  {
    "start_date": "2024-01-01",
    "end_date": "2024-02-01"
  }
  ```
- **Response**: An Excel file (`filtered_sales_report.xlsx`).

---

## 🖥️ UI Screenshots

(Add images of your UI using Markdown)

```md
![Home Page](screenshots/home.png)
![Filter Form](screenshots/filter.png)
```

---

## ⚡ Future Improvements

- Add user authentication
- Support for multiple file formats (CSV, JSON)
- Cloud storage integration

---

## 🤝 Contributing

Feel free to create a pull request or open an issue.

---

## 📜 License

This project is licensed under the MIT License.




