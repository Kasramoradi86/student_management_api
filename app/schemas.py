from pydantic import BaseModel,EmailStr

class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    
class StudentCreate(StudentBase):
    classroom_id: int

class StudentResponse(StudentBase):
    id: int 
    classroom_id: int
    class Config:
        from_attributes = True

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: str | None = None
    classroom_id: int | None = None


class ClassRoomBase(BaseModel):
    name: str

class ClassRoomCreate(ClassRoomBase):
    pass

class ClassRoomResponse(ClassRoomBase):
    id: int
    class Config:
        from_attributes = True

class ClassRoomUpdate(ClassRoomBase):
    pass