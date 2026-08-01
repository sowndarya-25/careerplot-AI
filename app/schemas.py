from pydantic import BaseModel, EmailStr


# Request schema for user registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# Response schema after registration
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


# Request schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response schema for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

   