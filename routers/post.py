from fastapi import APIRouter, Depends, UploadFile, File
from typing import List
from routers.schemas import UserAuth, PostDisplay, UserBase, PostBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from auth.oauth2 import get_current_user
from db import db_post

import random
import string
import shutil

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('/', response_model=PostDisplay)
def add_post(request: PostBase, db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_post.create_post(db, current_user, request)

@router.get('/myposts', response_model=List[PostDisplay])
def get_my_posts(db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_post.get_posts_by_id(db, current_user)

@router.get('/followuserposts', response_model=List[PostDisplay])
def get_follow_user_posts(db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_post.get_follow_user_posts(db, current_user)

@router.post('/image')
def add_image(image: UploadFile=File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}
