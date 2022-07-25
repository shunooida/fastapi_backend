from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_message
from routers.schemas import MessageBase, MessageDisplay
from routers.schemas import UserAuth
from auth.oauth2 import get_current_user
from typing import List

router = APIRouter(
    prefix='/message',
    tags=['message']
)

@router.get('/{with_user_id}', response_model=List[MessageDisplay])
def get_messages(with_user_id: int, db: Session=Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_message.get_friend_messages(db, with_user_id, current_user)

@router.post('/{to_user_id}', response_model=MessageDisplay)
def send_message(to_user_id: int, request: MessageBase, db: Session=Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_message.create_message(db, to_user_id, request, current_user)