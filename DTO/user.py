from pydantic import BaseModel,ValidationError,Field

class UserSchema(BaseModel):
    name:str = Field(...,min_length=3,max_length=20)
    model_config = {"extra": "forbid"}


