from fastapi import Request,status
from fastapi.responses import JSONResponse
from .exceptions import StudentNotFoundException,ClassRoomNotFoundException

async def student_not_found_handler(request : Request , exc : StudentNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"detail":f"Student with id {exc.student_id} not found"})

async def classroom_not_found_handler(request : Request , exc : ClassRoomNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"datail": f"Classroom with id {exc.classroom_id} not found"})

