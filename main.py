from fastapi import FastAPI

from db import database
from db import models
from routers import user, message

app = FastAPI()

app.include_router(user.router)
app.include_router(message.router)

@app.get('/')
def index():
    return 'hello my project'

models.database.Base.metadata.create_all(database.engine)

#main file