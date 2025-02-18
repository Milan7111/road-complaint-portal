from fastapi import FastAPI
from routes.complaints import router as complaints_router
from routes.users import router as users_router

app = FastAPI()

# Include existing routers
app.include_router(complaints_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Road Complaint Portal"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from routes.auth import router as auth_router  # Keep existing auth routes

app = FastAPI()

# Include authentication routes
app.include_router(auth_router)

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection (Modify credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",  # Change this to your MySQL password
    database="road_complaints"
)
cursor = conn.cursor(dictionary=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to Road Complaint Portal"}

# API endpoint to fetch complaints
@app.get("/complaints")
def get_complaints():
    cursor.execute("SELECT id, description, latitude, longitude, image_url FROM complaints")
    return cursor.fetchall()

# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
