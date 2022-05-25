from sqlalchemy.orm.session import Session

from db.models import DbMessage
from routers.schemas import MessageBase

def create_message(db: Session, to_user_id: int, request: MessageBase):
    new_message = DbMessage(
        from_user_id = request.from_user_id,
        to_user_id = to_user_id,
        message = request.message,
        is_read = request.is_read
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message