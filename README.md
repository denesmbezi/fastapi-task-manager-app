# 📝 FastAPI Task Manager API

A simple and modern Task Manager API built with **FastAPI** and **MongoDB**. This project allows users to register, authenticate, and manage personal tasks — including creating, reading, updating, deleting, and filtering tasks by status or due date.

---

## 🚀 Features

- 🔐 **JWT Authentication** (Register/Login)
- 🧾 **Task Management** (CRUD)
- 🔍 **Filtering** by status and due date
- 📄 **Swagger API Docs** (`/docs`)
- ⚙️ **Async MongoDB (Motor)** integration
- 📦 Modular and scalable project structure
- 🐳 Docker-ready (optional)

---

## 🛠️ Tech Stack

| Tool        | Purpose                       |
|-------------|-------------------------------|
| FastAPI     | Web framework (Python)        |
| Motor       | Async MongoDB driver          |
| Pydantic    | Data validation               |
| Python-Jose | JWT handling                  |
| Uvicorn     | ASGI server                   |
| MongoDB     | Document-based database       |

---

## 📁 Project Structure

task-manager-api/
│
├── app/
│ ├── main.py # Entry point
│ ├── database.py # MongoDB connection
│ ├── models.py # Pydantic models
│ ├── auth.py # JWT auth logic
│ ├── routes/
│ │ ├── users.py # Register/Login routes
│ │ └── tasks.py # Task routes
│ └── utils.py # Helper functions
│
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md



---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/denesmbezi/fastapi-task-manager-app.git
cd fastapi-task-manager-app


2. Create Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Requirements
   pip install -r requirements.txt

4. Set Environment Variables
   Create a .env file:

   MONGO_URI=mongodb://localhost:27017
   JWT_SECRET=your_jwt_secret_key
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Run the App
   uvicorn app.main:app --reload

