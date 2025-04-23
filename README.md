# ✈️ Airline Ticketing API

A RESTful API for managing airline ticketing operations including flight creation, ticket purchase, check-in, and passenger listing — developed with Flask, SQLAlchemy, JWT authentication, PostgreSQL, and Swagger documentation.

---

- **Swagger UI:**  https://airline-project-227h.onrender.com/apidocs
---

## 📦 Features

- ✅ Add Flights (admin only)
- ✅ Flight Search with paging
- ✅ Ticket Purchase with seat availability control
- ✅ Check-in with seat assignment
- ✅ Passenger List per Flight
- ✅ JWT-based Authentication
- ✅ Swagger UI for testing

---

## 🧠 Assumptions

- Flights can only be added by admin users
- Customers must register before buying tickets
- Seat numbers are assigned in order during check-in
- JWT authentication required for protected endpoints

> 🔐 **Default Admin Credentials:**
> - Username: `admin`
> - Password: `1234`

---

## 🗂️ Project Structure
Airline_Project/ ├── app/ │ ├── init.py │ ├── config.py │ ├── models/ │ ├── routes/ │ ├── services/ │ ├── schemas/ │ └── utils/ ├── run.py ├── requirements.txt └── README.md

---

## 🧪 Technologies Used

- Python & Flask
- PostgreSQL (Render.com)
- SQLAlchemy
- JWT Authentication
- Flasgger (Swagger UI)
- dotenv for secure configs

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/ysgmur/Airline_Project.git
cd Airline_Project
python -m venv venv
source venv/bin/activate (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
DATABASE_URL=postgresql://your_user:your_pass@your_host/db
JWT_SECRET_KEY=super-secret-key

Issues Encountered
GitGuardian warning for exposed DB URI (fixed by using .env)
Swagger token auth not visible until added securityDefinitions
PostgreSQL URI had to be manually encoded due to special characters
Merge conflict caused temporary project loss, project was fully rebuilt.
Swagger authorize button occasionally didn't show in Render deployment.




