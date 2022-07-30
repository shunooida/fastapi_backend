from fastapi import APIRouter, Depends
from typing import List
from routers.schemas import FriendDisplay, UserAuth
from sqlalchemy.orm.session import Session
from db.database import get_db
from auth.oauth2 import get_current_user
from db import db_friend

router = APIRouter(
    prefix='/friend',
    tags=['friend']
)

@router.get('/', response_model=List[FriendDisplay])
def get_my_friends(db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_friend.get_my_friends(db, current_user)

@router.post('/delete/{user_id}}')
def unfollow(user_id: int, db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_friend.delete_friend(db, user_id, current_user)

#postメソッドでいいのかを検討
@router.post('/{to_user_id}')
def make_frined(to_user_id: int, db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_friend.create_friend(db, to_user_id, current_user)