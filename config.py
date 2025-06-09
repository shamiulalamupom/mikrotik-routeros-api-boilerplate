import os
from dotenv import load_dotenv

load_dotenv()

class MikrotikConfig:
    HOST = os.getenv("MIKROTIK_HOST")
    USERNAME = os.getenv("MIKROTIK_USERNAME")
    PASSWORD = os.getenv("MIKROTIK_PASSWORD")
    PORT = int(os.getenv("MIKROTIK_PORT", 8729))
    USE_SSL = False
    PLAIN_TEXT_LOGIN = True

class MongoConfig:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DBNAME = os.getenv("MONGO_DBNAME", "easeconnect")

class JWTConfig:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES"))  # 24 hours