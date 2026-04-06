from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return{"Status: ok"}

app.include_router(auth_router)