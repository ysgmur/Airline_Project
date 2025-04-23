
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

🐞 Issues Encountered
GitGuardian warning for exposed DB URI (fixed using .env)
Swagger token auth not visible until securityDefinitions added
PostgreSQL URI had to be encoded manually due to special characters
Merge conflict caused temporary project loss, then fully rebuilt
Swagger Authorize button sometimes doesn't show on Render (free tier)
