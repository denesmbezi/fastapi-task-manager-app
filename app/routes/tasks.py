from fastapi import APIRouter, HTTPException
from app.models import User
from app.database import mongodb
from app.schemas import serialize_doc
from app.models import Task, TaskStatus
from bson import ObjectId
app = APIRouter()




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



@app.patch("/task/{task_id}", status_code=200)
async def update_task(task_id: str, task: Task):
    result = await mongodb.db["tasks"].update_one({"_id": ObjectId(task_id)}, {"$set": task.dict()})
    if result.modified_count == 0:
        return {"message": "Task not found or no changes made"}
    updated_task = await mongodb.db["tasks"].find_one({"_id": ObjectId(task_id)})
    updated_task = serialize_doc(updated_task)
    return {"message": f"Task {updated_task['title']} updated successfully",
            "task": updated_task
            }

@app.delete("/task/{task_id}", status_code=200)
async def delete_task(task_id: str):
    result = await mongodb.db["tasks"].delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task with ID {task_id} deleted successfully"}


@app.put("/task/{task_id}/status", status_code=200)
async def set_task_status(task_id: str, status: TaskStatus):
    valid_statuses = status
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    result = await mongodb.db["tasks"].update_one({"_id": ObjectId(task_id)}, {"$set": {"status": status}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Task not found or no changes made")
    
    updated_task = await mongodb.db["tasks"].find_one({"_id": ObjectId(task_id)})
    updated_task = serialize_doc(updated_task)
    return {"message": f"Task {updated_task['title']} status updated to {status}",
            "task": updated_task
            }
