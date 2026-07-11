from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    email = Column(String,nullable=True,unique=True)
    classroom_id = Column(Integer,ForeignKey("classrooms.id"))
    
    classroom = relationship("Classroom",back_populates="students")

class Classroom(Base):
    __tablename__ = "classrooms"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)

    students = relationship("Student",back_populates="classroom")