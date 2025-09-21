 Flask Auth + JWT + Redis Rate Limiting Backend

## 📌 Overview
This project is a **Flask-based backend service** with:

- **User authentication** (registration, login) with password hashing
- **JWT (JSON Web Token)** based authentication for protected routes
- **Refresh tokens** for renewing access without re-login
- **PostgreSQL** integration via SQLAlchemy
- **Redis caching** for faster responses on expensive operations
- **API rate limiting** using Flask-Limiter with Redis backend for persistence

It is designed for learning purposes and is not production-hardened.

---

## 🗂 Tech Stack
- **Python 3.11**
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- PostgreSQL
- Redis
- Flask-Limiter

---

## ⚙️ Environment Variables
Before running, set these environment variables with your own values:
bash export DATABASE_URL="postgresql+psycopg2://user:password@host/dbname?sslmode=require" export JWT_SECRET_KEY="your_jwt_secret_key" export REDIS_URL="redis://default:password@redis-host:6379"

You can also store them in a `.env` file (don’t commit it to GitHub).

---

## 📦 Installation
1. **Clone the repository**
bash git clone https://github.com/your-username/your-repo.git cd your-repo

2. **Install dependencies**
bash pip install -r requirements.txt

3. **Set environment variables**
bash export DATABASE_URL="..." export JWT_SECRET_KEY="..." export REDIS_URL="..."

4. **Run the Flask server**
bash flask run

---

## 🚀 API Endpoints

| Method | Endpoint       | Description |
|--------|---------------|-------------|
| POST   | `/register`   | Register a new user |
| POST   | `/login`      | Authenticate user, get access + refresh tokens |
| GET    | `/protected`  | Example protected route (JWT access token required) |
| POST   | `/refresh`    | Refresh access token using refresh token |
| GET    | `/expensive`  | Cached and rate-limited sample endpoint |

---

## 🔒 Security Notes
- **Never** hardcode your DB credentials or JWT secret in code.
- Use environment variables for secrets.
- HTTPS is recommended for production.

---

## 🧑‍💻 Example Usage:
**Login and access protected route**
bash curl -X POST http://localhost:5000/login
-H "Content-Type: application/json"
-d '{"username":"alice","password":"secret"}'

Using the returned access token
curl -X GET http://localhost:5000/protected
-H "Authorization: Bearer YOUR_ACCESS_TOKEN"

---

## 📜 License
MIT License – Feel free to use and modify for learning.
