from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URI="mongodb://localhost:27017"
MONGO_DB="task_db"

if not MONGO_URI or not MONGO_DB:
    raise ValueError("MONGO_URI and MONGO_DB must be set in the environment variables.")

class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[MONGO_DB]

    async def close(self):
        self.client.close()
        await self.client.close()

mongodb = MongoDB()

