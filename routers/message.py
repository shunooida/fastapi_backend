from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_message
from routers.schemas import MessageBase, MessageDisplay

router = APIRouter(
    prefix='/message',
    tags=['message']
)

@router.post('/{to_user_id}', response_model=MessageDisplay)
def send_message(to_user_id: int, request: MessageBase, db: Session=Depends(get_db)):
    return db_message.create_message(db, to_user_id, request)