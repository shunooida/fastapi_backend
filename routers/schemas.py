from pydantic import BaseModel
from typing import List

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
    message: str

class MessageDisplay(BaseModel):
    from_user_id: int
    to_user_id: int
    message: str
    is_read: bool
    class Config():
        orm_mode = True

class FriendBase(BaseModel):
    username: str

class FriendDisplay(BaseModel):
    id: int
    username: str
    authenticated: bool

    class Config():
        orm_mode = True

class UserAuth(BaseModel):
    id: int
    username: str
    email: str