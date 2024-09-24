from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True,nullable=False)
    # username=Column(String,unique=True,nullable=False) as of now  email will be considered as the username
    email=Column(String,unique=True,nullable=False)
    password=Column(String)#hashed password 
    is_active=Column(Boolean,default=True)


class Lost_items(Base):
    __tablename__="lost_items"   

    id=Column(Integer,primary_key=True,nullable=False)
    item_name=Column(String,nullable=False)
    description=Column(String)
    location_lost=Column(String)
    date_lost=Column(datetime,default=datetime.uctnow)

    # defining relations between user table and lost_items table
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="lost_items")

class Found_items(Base):
    __table__name='found_items'
    id=Column(Integer,primary_key=True,nullable=False)
    item_name=Column(String,nullable=False)
    description=Column(String)
    location_found=Column(String)
    date_found=Column(datetime,default=datetime.uctnow)

    # defining relations between user table and found_items table
    finder_id = Column(Integer, ForeignKey("users.id"))
    finder = relationship("User", back_populates="found_items")


