from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

app = FastAPI()

# Step 1: This is your "security dependency"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Step 2: Fake user database for demonstration
fake_users_db = {
    "alice": {
        "username": "alice",
        "password": "wonderland",  # NOTE: Never store plain text in real life
        "token": "secrettoken123"
    }
}


# Step 3: Token endpoint — where clients send username/password to get a token
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = fake_users_db.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return {
        "access_token": user["token"],
        "token_type": "bearer"
    }


# Step 4: Protected endpoint — requires valid token
@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    # Normally you'd verify the token here (e.g., decode JWT)
    for user in fake_users_db.values():
        if token == user["token"]:
            return {"message": f"Welcome, {user['username']}", "token": token}

    raise HTTPException(status_code=401, detail="Invalid token")
