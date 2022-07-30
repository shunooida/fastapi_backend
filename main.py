from fastapi import FastAPI

from db import database
from db import models
from routers import user, message, friend, post, story
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(message.router)
app.include_router(friend.router)
app.include_router(post.router)
app.include_router(story.router)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.database.Base.metadata.create_all(database.engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
app.mount('/stories', StaticFiles(directory='stories'), name='stories')
