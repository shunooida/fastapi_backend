from sqlalchemy.orm.session import Session
from routers.schemas import UserAuth
from sqlalchemy import and_, or_
from db.models import DbFriend, DbUser

def create_friend(db: Session, to_user_id, current_user: UserAuth):
    new_friend = DbFriend(
        from_user_id = current_user.id,
        to_user_id = to_user_id,
        authenticated = False
    )
    db.add(new_friend)
    db.commit()
    db.refresh(new_friend)
    return

def delete_friend(db: Session, user_id, current_user: UserAuth):
    delete_friend = db.query(DbFriend).filter(
        DbFriend.from_user_id == current_user.id,
        DbFriend.to_user_id == user_id
    ).first()
    db.delete(delete_friend)
    db.commit()
    return

def get_my_friends(db: Session, current_user: UserAuth):
    return db.query(DbUser).join(
        DbFriend,
        or_(
            and_(
                DbFriend.to_user_id == DbUser.id,
                DbFriend.from_user_id == current_user.id
            ),
            and_(
                DbFriend.to_user_id == current_user.id,
                DbFriend.from_user_id == DbUser.id
            )
        )
    ).with_entities(
        DbUser.id, DbUser.username, DbFriend.authenticated
    ).all()