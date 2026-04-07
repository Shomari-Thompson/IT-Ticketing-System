from fastapi import FastAPI
from app.db.database import Base, engine
from app.models.user import User
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return{"Status: ok"}

app.include_router(auth_router)