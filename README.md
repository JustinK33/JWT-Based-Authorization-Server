 Flask Auth + JWT + Redis Rate Limiting Backend

## 📌 Overview
**Flask-based backend service** with:

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

## 🚀 API Endpoints

| Method | Endpoint       | Description |
|--------|---------------|-------------|
| POST   | `/register`   | Register a new user |
| POST   | `/login`      | Authenticate user, get access + refresh tokens |
| GET    | `/protected`  | Example protected route (JWT access token required) |
| POST   | `/refresh`    | Refresh access token using refresh token |
| GET    | `/expensive`  | Cached and rate-limited sample endpoint |

---

## 📜 License
MIT License – Feel free to use and modify for learning.
