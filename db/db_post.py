from sqlalchemy.orm.session import Session
from routers.schemas import UserAuth, PostBase
from db.models import DbPost, DbFriend
from sqlalchemy import and_

def get_posts_by_id(db: Session, current_user: UserAuth):
    return db.query(DbPost).filter(
                DbPost.user_id == current_user.id
            ).order_by(DbPost.id).all()

def create_post(db: Session, current_user: UserAuth, request: PostBase):
    new_post = DbPost(
        image_path = request.image_path,
        caption = request.caption,
        user_id = current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def delete_post(post_id: int, db: Session, current_user: UserAuth):
    delete_post = db.query(DbPost).filter(
        DbPost.id == post_id
    ).first()
    db.delete(delete_post)
    db.commit()
    return

def get_follow_user_posts(db: Session, current_user: UserAuth):
    sub_query = db.query(DbFriend).filter(
            and_(
                DbFriend.to_user_id == DbPost.user_id,
                DbFriend.from_user_id == current_user.id
            )     
    )
    return db.query(DbPost).filter(sub_query.exists()).with_entities(DbPost.id, DbPost.image_path, DbPost.caption).all()
    

    