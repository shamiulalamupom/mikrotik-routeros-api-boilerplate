from motor.motor_asyncio import AsyncIOMotorClient
from config import MongoConfig

client = AsyncIOMotorClient(MongoConfig.MONGO_URI)
db = client.get_default_database(MongoConfig.MONGO_DBNAME)

user_collection = db.users