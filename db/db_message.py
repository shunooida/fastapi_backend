from sqlalchemy.orm.session import Session

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