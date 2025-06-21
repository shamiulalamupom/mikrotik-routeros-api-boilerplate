from pydantic import BaseModel, Field

class UserRegistrationSchema(BaseModel):
    username: str = Field(..., description="The username of the user")
    password: str = Field(..., description="The password of the user")
    email: str = Field(..., description="The email address of the user")

class UserLoginSchema(BaseModel):
    username: str = Field(..., description="The username of the user")
    password: str = Field(..., description="The password of the user")