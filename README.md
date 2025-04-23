# ✈️ Airline Ticketing API

A RESTful API for managing airline ticketing operations including flight creation, ticket purchase, check-in, and passenger listing — developed with Flask, SQLAlchemy, JWT authentication, PostgreSQL, and Swagger documentation.

---

### 🔗 Source Code

👉 [Airline Ticketing API - GitHub Repository](https://github.com/ysgmur/Airline_Project)

---

### 🎥 Project Demo Video

▶️ [Watch the video here](https://drive.google.com/file/d/1AlxHvJsv9N3yzEX0g-ZWJBOIb8_LIwVS/view?usp=sharing)

---

### 📚 Swagger Documentation

Explore and test the API endpoints:

🔗 [Swagger UI](https://airline-project-227h.onrender.com/apidocs/#/)

> ⚠️ **Note:** This project is hosted on Render (free tier).  
> Server sleeps after 15 minutes of inactivity and may take up to 1 minute to wake up.

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

### 📌 ER Diagram

![ER Diagram](https://github.com/ysgmur/Airline_Project/blob/main/ER_Diagram/ER%20Diagram.png?raw=true)

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
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Set environment variables
DATABASE_URL=postgresql://your_user:your_pass@your_host/db
JWT_SECRET_KEY=super-secret-key

---
## 🐞 Issues Encountered
GitGuardian warning for exposed DB URI (fixed using .env)
Swagger token auth not visible until securityDefinitions added
PostgreSQL URI had to be encoded manually due to special characters
Merge conflict caused temporary project loss, then fully rebuilt
Swagger Authorize button sometimes doesn't show on Render (free tier)



