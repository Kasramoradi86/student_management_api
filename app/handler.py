from fastapi import Request,status
from fastapi.responses import JSONResponse
from .exceptions import StudentNotFoundException,ClassRoomNotFoundException,ClassRoomHasStudentException,StudentAlreadyInClassroomException

async def student_not_found_handler(request : Request , exc : StudentNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"detail":f"Student with id {exc.student_id} not found"})

async def classroom_not_found_handler(request : Request , exc : ClassRoomNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"datail": f"Classroom with id {exc.classroom_id} not found"})


async def classroom_has_student_handler(request : Request , exc : ClassRoomHasStudentException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"detail":f"Classroom with id {exc.classroom_id} has some students"})

async def student_already_in_classroom_handler(request : Request , exc : StudentAlreadyInClassroomException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST , content={"detail":f"Student with id {exc.student_id} is already in classroom with id {exc.classroom_id}"})