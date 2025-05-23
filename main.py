from typing import Annotated
from fastapi import Depends, FastAPI
from app.models import User, Task
from app.database import mongodb
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc



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
     

@app.post("/task/", status_code=200)
async def create_task(task: Task):
    existed_task = await mongodb.db["tasks"].find_one({"task": task.title})
    if existed_task:
        return {"message": f"Task {task.title} already exists"}
    result = await mongodb.db["tasks"].insert_one(task.dict())
    task = await mongodb.db["tasks"].find_one({"_id": result.inserted_id})
    task = serialize_doc(task)
    return {"message": f"Task {task['title']} created successfully",
            "task_id": str(result.inserted_id)
            }


@app.get("/tasks/")
async def get_tasks():
    tasks = []
    async for task in mongodb.db["tasks"].find():
        tasks.append(serialize_doc(task))
    return {"tasks": tasks}
