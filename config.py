import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:pass@host/dbname')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'change-me')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')