from pydantic import BaseModel,ValidationError,Field,EmailStr

class UserSchema(BaseModel):
    first_name:str = Field(...,min_length=2,max_length=30)
    second_name:str = Field(...,min_length=2,max_length=30)
    email:EmailStr | None = Field(default=None)
    password:str = Field(...,min_length=4,max_length=20)
    model_config = {"extra": "forbid"}


