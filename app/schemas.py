from pydantic import BaseModel,EmailStr

class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    
class StudentCreate(StudentBase):
    classroom_id: int

class StudentSimpleResponse(StudentBase):
    id: int 
    classroom_id: int
    class Config:
        from_attributes = True

class StudentResponse(StudentBase):
    id: int
    classroom: "ClassRoomSimpleResponse"
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

class ClassRoomSimpleResponse(ClassRoomBase):
    id: int

    class Config:
        from_attributes = True

class ClassRoomResponse(ClassRoomBase):
    id:int 
    students: list[StudentSimpleResponse] = []
    class Config:
        from_attributes = True

class ClassRoomUpdate(ClassRoomBase):
    pass

StudentResponse.model_rebuild()
ClassRoomResponse.model_rebuild()