# 💼 SwiftBill – Automated Invoice Generator

SwiftBill is a lightweight web application that allows freelancers and small businesses to **generate professional PDF invoices** instantly. Built with Python and Flask, it offers a clean interface for entering client details and billing data, and it outputs print-ready invoices using the FPDF2 library. All invoices are saved locally, with optional features to track, filter, and email them.

---

## 🚀 Features

- 📝 Input form for client, item, and tax details  
- 🧮 Auto-calculation of totals, tax, and discounts  
- 📄 Generate clean, styled PDF invoices with your branding  
- 🗂️ View history of saved invoices  
- 💾 Store invoice data in a lightweight SQLite database  
- 📧 (Optional) Email invoices directly to clients  
- 🔐 (Optional) Add basic login authentication for secure access

---

## 🛠️ Tech Stack

| Layer         | Tools Used                       |
|--------------|----------------------------------|
| Backend       | Python, Flask                    |
| PDF Engine    | FPDF2                            |
| Database      | SQLite (via SQLAlchemy - optional) |
| Frontend      | HTML, CSS, Bootstrap             |
| Deployment    | Render / Railway / PythonAnywhere |

---

## 📁 Folder Structure
SwiftBill/
├── app/
│ ├── static/
│ ├── templates/
│ ├── init.py
│ └── routes.py
├── invoices/ # PDF output directory
├── database/ # DB file (invoices.db)
├── main.py # Entry point
├── requirements.txt
└── README.md

## ⚙️ How to Run Locally
1. **Clone the repository**
   git clone https://github.com/dinesh20121993/SwiftBill.git
   cd SwiftBill
2. **Create virtual environment & activate**
  python3 -m venv venv
  source venv/bin/activate
3. **Install dependencies**
  pip install -r requirements.txt
4. **Run the app**
  python main.py
5. **Visit http://127.0.0.1:5000 in your browser.**
