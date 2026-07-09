from fastapi import FastAPI
from .database import engine
from . import models
from .routers import classroom 

app = FastAPI(title="Student Management API",description="A simple REST API for student management built with FASTAPI",version="1.0.0")
app.include_router(classroom.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"massage":"Student Management API is running"}