from fastapi import APIRouter, Depends, UploadFile, File
from routers.schemas import StoryDisplay, StoryBase, UserAuth
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db import db_story
from db.database import get_db

router = APIRouter(
    prefix='/story',
    tags=['story']
)

@router.post('/')
def add_story(request: StoryBase, db: Session=Depends(get_db), current_user: UserAuth=Depends(get_current_user)):
    return db_story.create_story_path(request, db, current_user)

@router.post('/movie')
def add_movie(movie: UploadFile=File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'stories/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}