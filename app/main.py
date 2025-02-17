from fastapi import FastAPI
from routes.auth import router as auth_router  # Import your auth routes

app = FastAPI()

# Include authentication routes
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Road Complaint Portal"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
