from pydantic import BaseModel,Field,EmailStr

class AdminSchema(BaseModel):
    login:str = Field(...,min_length=2,max_length=30)
    password:int = Field(...,min_length=4,max_length=30)
    email: EmailStr | None = Field(default=None)