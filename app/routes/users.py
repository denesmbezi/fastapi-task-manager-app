from fastapi import APIRouter, HTTPException
from app.models import User
from app.database import mongodb
from app.schemas import serialize_doc


app = APIRouter()

@app.post("/user/", response_model=None)
async def create_user(user: User):
    existed_user = await mongodb.db["users"].find_one({"email": user.email})
    if existed_user:
        return {"message": f"User {user.email} already exists"}
    # if not existed_user:
    #     return {"message": f"User {user.email} does not exist"}
    result = await mongodb.db["users"].insert_one(user.dict())
    return {"message": f"User {user.full_name} created successfully",
            "user_id": str(result.inserted_id)
            }


@app.get("/users/")
async def get_users():
    users = []
    async for user in mongodb.db["users"].find():
        users.append(serialize_doc(user))
    return {"users": users}