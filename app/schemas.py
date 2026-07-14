from pydantic import BaseModel,EmailStr,Field,field_validator
import re

class StudentBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        examples=["Kasra moradi"]
    )
    age: int = Field(
        ge=6,
        le=120,
        examples=[20]
    )
    email: EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value : str) -> str:
        value = " ".join(value.split())
        value = value.title()
        if not value:
            raise ValueError("Student name can not be empty")
        if not re.fullmatch(r"^[A-Za-z ]+$",value):
            raise ValueError("Name must contain only letters")
        return value

    @field_validator("email")
    @classmethod
    def normalize_email(cls , value: str) -> str:
        return value.strip().lower()

class StudentCreate(StudentBase):
    classroom_id: int = Field(ge=1)

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
    name: str | None = Field(default=None,min_length=2,max_length=50,examples=["Kasra Moradi"])
    age: int | None = Field(default=None,ge=6,le=120,examples=[20])
    email: EmailStr | None = None
    classroom_id: int | None = Field(default=None,ge=1)

    @field_validator("name")
    @classmethod
    def validate_name(cls , value:str) -> str:
        if value is None:
            return value
        value = " ".join(value.split())
        value = value.title()
        if not re.fullmatch(r"^[A-Za-z ]+$",value):
            raise ValueError("Name must contain only letters")
        return value
    
    @field_validator("email")
    @classmethod
    def normalize_email(cls , value):
        if value is None:
            return value
        return value.strip().lower()

class ClassRoomBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        examples=["Python Basics"]
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls , value:str) -> str:
        value = " ".join(value.split())
        value = value.title()
        if not value :
            raise ValueError("Classroom name can not be empty")
        return value

class ClassRoomCreate(ClassRoomBase):
    pass

class ClassRoomSimpleResponse(ClassRoomBase):
    id: int

    class Config:
        from_attributes = True

class ClassRoomResponse(ClassRoomBase):
    id:int 
    students: list[StudentSimpleResponse] = Field(default_factory=list)

    class Config:
        from_attributes = True

class ClassRoomUpdate(ClassRoomBase):
    pass

StudentResponse.model_rebuild()
ClassRoomResponse.model_rebuild()