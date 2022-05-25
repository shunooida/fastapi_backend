from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True

class MessageBase(BaseModel):
    from_user_id: int
    message: str
    is_read: bool

class MessageDisplay(BaseModel):
    from_user_id: int
    to_user_id: int
    message: str
    is_read: bool
    class Config():
        orm_mode = True