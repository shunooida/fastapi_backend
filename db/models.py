from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import database


class DbUser(database.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    #message = relationship('DbMessage', back_populates='message')
    #friend = relationship('DbFriend', back_populates='friend')

class DbMessage(database.Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    to_user_id = Column(Integer, ForeignKey('user.id'))
    message = Column(String)
    is_read = Column(Boolean)
    #user = relationship('DbUser', back_populates='user')

class DbFriend(database.Base):
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    to_user_id = Column(Integer, ForeignKey('user.id'))
    authenticated = Column(Boolean)
    #user = relationship('DbUser', back_populates='user')