from pydantic import BaseModel,EmailStr



class Token(BaseModel):
    token:str
    token_type:str 
