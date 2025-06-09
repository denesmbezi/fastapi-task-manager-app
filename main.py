from typing import Annotated
from fastapi import Depends, FastAPI
from app.models import User, Task
from app.database import mongodb
from bson import ObjectId
from app.schemas import serialize_doc
from app.routes.users import app as users_router
from app.routes.tasks import app as tasks_router


app = FastAPI()
@app.on_event("startup")
async def startup_event():
    pass
    #await mongodb.init_mongodb()

@app.on_event("shutdown")
async def shutdown_event():
    pass
    #await mongodb.close_mongodb()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])