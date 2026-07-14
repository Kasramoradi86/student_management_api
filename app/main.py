from fastapi import FastAPI
from .database import engine
from . import models
from .routers import classroom,student
from .exceptions import StudentNotFoundException,ClassRoomNotFoundException
from .handler import student_not_found_handler,classroom_not_found_handler

app = FastAPI(title="Student Management API",description="A simple REST API for student management built with FASTAPI",version="1.0.0")
app.include_router(classroom.router)
app.include_router(student.router)
models.Base.metadata.create_all(bind=engine)
app.add_exception_handler(StudentNotFoundException,student_not_found_handler)
app.add_exception_handler(ClassRoomNotFoundException,classroom_not_found_handler)

@app.get("/")
def root():
    return {"massage":"Student Management API is running"}