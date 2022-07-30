from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import database


class DbUser(database.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class DbMessage(database.Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    to_user_id = Column(Integer, ForeignKey('user.id'))
    message = Column(String)
    is_read = Column(Boolean)

class DbFriend(database.Base):
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    to_user_id = Column(Integer, ForeignKey('user.id'))
    authenticated = Column(Boolean)

class DbPost(database.Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image_path = Column(String)
    caption = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

class DbStory(database.Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    story_path = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))