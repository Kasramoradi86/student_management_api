from sqlalchemy.orm import Session
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