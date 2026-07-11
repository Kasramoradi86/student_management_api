from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,crud
from ..dependencies import get_db

router = APIRouter(prefix="/students",tags=["Students"])

@router.post("/",response_model=schemas.StudentSimpleResponse,status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate,db:Session = Depends(get_db)):
    return crud.create_student(db=db,student=student)

@router.get("/",response_model=list[schemas.StudentSimpleResponse],status_code=status.HTTP_200_OK)
def get_all_students(db:Session = Depends(get_db)):
    return crud.get_all_students(db=db)

@router.get("/{student_id}",response_model=schemas.StudentResponse,status_code=status.HTTP_200_OK)
def get_student_by_id(student_id:int, db:Session = Depends(get_db)):
    student = crud.get_student_by_id(student_id=student_id,db=db)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")
    else:
        return student
    
@router.put("/{student_id}",response_model=schemas.StudentSimpleResponse,status_code=status.HTTP_200_OK)
def update_student(student_id:int,student:schemas.StudentUpdate,db:Session = Depends(get_db)):
    update_student = crud.update_student(student_id=student_id,student_data=student,db=db)
    if update_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return update_student
    
@router.delete("/{student_id}",status_code=status.HTTP_200_OK)
def delete_student(student_id:int,db:Session = Depends(get_db)):
    student_deleted = crud.delete_student(student_id=student_id,db=db)
    if student_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")
    else:
        return {"massage":"Student deleted successfully"}