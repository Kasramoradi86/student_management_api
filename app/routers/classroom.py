from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import crud,schemas
from ..dependencies import get_db
from ..exceptions import ClassRoomNotFoundException

router = APIRouter(prefix="/classrooms",tags=["ClassRooms"])

@router.post("/",response_model=schemas.ClassRoomSimpleResponse,status_code=status.HTTP_201_CREATED)
def create_classroom(classroom:schemas.ClassRoomCreate,db:Session = Depends(get_db)):
    return crud.create_classroom(db=db,classroom=classroom)

@router.get("/",response_model=list[schemas.ClassRoomSimpleResponse],status_code=status.HTTP_200_OK)
def get_all_classrooms(db:Session = Depends(get_db)):
    return crud.get_all_classrooms(db=db)

@router.get("/{classroom_id}",response_model=schemas.ClassRoomResponse,status_code=status.HTTP_200_OK)
def get_classroom(classroom_id:int,db:Session = Depends(get_db)):
    classroom = crud.get_classroom_by_id(db=db,id=classroom_id)
    if classroom is None:
        raise ClassRoomNotFoundException(classroom_id)
    return classroom

@router.put("/{classroom_id}",response_model=schemas.ClassRoomSimpleResponse,status_code=status.HTTP_200_OK)
def update_classroom(classroom_id:int,classroom:schemas.ClassRoomUpdate,db:Session = Depends(get_db)):
    classroom_updated = crud.update_classroom(db=db,classroom_id=classroom_id,classroom_data=classroom)
    if classroom_updated is None:
        raise ClassRoomNotFoundException(classroom_id)
    return classroom_updated

@router.delete("/{classroom_id}",status_code=status.HTTP_200_OK)
def delete_classroom(classroom_id:int,db:Session = Depends(get_db)):
    classroom_deleted = crud.delete_classroom(db=db,classroom_id=classroom_id)
    if classroom_deleted is None:
        raise ClassRoomNotFoundException(classroom_id)
    else:
        return {"massage":"Classroom deleted successfully"}
