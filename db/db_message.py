from sqlalchemy.orm.session import Session
from sqlalchemy import or_, and_

from db.models import DbMessage
from routers.schemas import MessageBase, UserAuth

def create_message(db: Session, to_user_id: int, request: MessageBase, current_user: UserAuth):
    new_message = DbMessage(
        from_user_id = current_user.id,
        to_user_id = to_user_id,
        message = request.message,
        is_read = False
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_friend_messages(db: Session, friend_id: int, current_user: UserAuth):
    return db.query(DbMessage).filter(
        or_(
            and_(
                DbMessage.from_user_id == current_user.id,
                DbMessage.to_user_id == friend_id),
            and_(
                DbMessage.from_user_id == friend_id,
                DbMessage.to_user_id == current_user.id)
            )
        ).order_by(DbMessage.id).all()