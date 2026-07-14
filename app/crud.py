from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from . import schemas,models

def create_classroom(db: Session,classroom: schemas.ClassRoomCreate):
    db_classroom = models.Classroom(name=classroom.name)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def get_all_classrooms(db:Session):
    return db.query(models.Classroom).all()

def get_classroom_by_id(db:Session,id:int):
    return (db.query(models.Classroom).filter_by(id=id)).first()

def update_classroom(db:Session,classroom_id:int,classroom_data:schemas.ClassRoomUpdate):
    classroom = get_classroom_by_id(db=db,id=classroom_id)
    if classroom is not None:
        classroom.name = classroom_data.name
        db.commit()
        db.refresh(classroom)
        return classroom
    else:
        return None

def delete_classroom(db:Session,classroom_id:int):
    classroom = get_classroom_by_id(db=db,id=classroom_id)
    if classroom is not None:
        db.delete(classroom)
        db.commit()
        return classroom
    else:
        return None
    
def create_student(db:Session,student:schemas.StudentCreate):
    classroom = db.query(models.Classroom).filter(models.Classroom.id == student.classroom_id).first()
    if classroom is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Classroom not found")
    db_student = models.Student(name=student.name,age=student.age,email=student.email,classroom_id=student.classroom_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students(db:Session):
    return db.query(models.Student).all()

def get_student_by_id(student_id:int,db:Session):
    return db.query(models.Student).filter_by(id=student_id).first()

def update_student(student_id:int,student_data:schemas.StudentUpdate,db:Session):
    if student_data.classroom_id is not None:
        classroom = db.query(models.Classroom).filter(models.Classroom.id == student_data.classroom_id).first()
        if classroom is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Classroom not found")
    db_student = get_student_by_id(student_id=student_id,db=db)
    if db_student is not None:
        update_data = student_data.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(db_student,key,value)
        db.commit()
        db.refresh(db_student)
        return db_student
    else:
        return None
    
def delete_student(student_id:int,db:Session):
    student = get_student_by_id(student_id=student_id,db=db)
    if student is not None:
        db.delete(student)
        db.commit()
        return student
    else:
        return None