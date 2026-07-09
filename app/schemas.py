from pydantic import BaseModel,EmailStr

class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    
class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int 
    classroom_id: int
    class Config:
        from_attributes = True


class ClassRoomBase(BaseModel):
    name: str

class ClassRoomCreate(ClassRoomBase):
    pass

class ClassRoomResponse(ClassRoomBase):
    id: int
    class Config:
        from_attributes = True