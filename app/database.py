from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient


# load environments from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")


class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[MONGO_DB]

    async def close(self):
        self.client.close()
        await self.client.close()

mongodb = MongoDB()


