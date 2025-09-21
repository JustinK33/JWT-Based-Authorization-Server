from flask import Flask, request
from sqlalchemy import text
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from redis import Redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from extensions import db
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'replace this'
app.config['JWT_SECRET_KEY'] = "replace this"

db.init_app(app)
jwt = JWTManager(app)
redis_client = Redis.from_url(app.config['REDIS_URL'])
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=app.config['REDIS_URL'],
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/")
@limiter.limit("50/day")
def home():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok"}, 200
    except Exception:
        app.logger.exception("DB health check failed")
        return {"status": "error"}, 500
    
@app.route("/register", methods=["POST"])
def register():
    from models import User
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter((User.username==username)|(User.email==email)).first():
        return {"error": "User already exists"}, 400
    
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {"message": "user successfully registered"}, 201

@app.route("/login", methods=["POST"])
def login():
    from models import User
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return {"error": "invalid username or password"}, 401
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return {"access_token": access_token, "refresh_token": refresh_token}, 200

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return {"message": f"Hello user {current_user_id}, you have access"},200

@app.route("/refresh", methods="POST")
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return {"access_token": new_access_token}, 200

@app.route("/expensive")
@limiter.limit("5/minute")
def expensive():
    cached = redis_client.get("expensive_result")
    if cached:
        return {"source": "cache", "result": cached.decode()}, 200

    result = "some computed value"
    redis_client.setex("expensive_result", 60, result)  # store for 60 seconds
    return {"source": "live", "result": result}, 200

if __name__ == "__main__":
    app.run(debug=True)
