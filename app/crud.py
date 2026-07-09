from sqlalchemy.orm import Session
from . import schemas,models

def create_classroom(db: Session,classroom: schemas.ClassRoomCreate):
    db_classroom = models.ClassRoom(name=classroom.name)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom