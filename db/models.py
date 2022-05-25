from sqlalchemy import Column, Integer, String, Boolean

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
    from_user_id = Column(Integer)
    to_user_id = Column(Integer)
    message = Column(String)
    is_read = Column(Boolean)