from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import crud,schemas
from ..dependencies import get_db

router = APIRouter(prefix="/classrooms",tags=["ClassRooms"])

@router.post("/",response_model=schemas.ClassRoomResponse)
def create_classroom(classroom:schemas.ClassRoomCreate,db:Session = Depends(get_db)):
    return crud.create_classroom(db=db,classroom=classroom)
