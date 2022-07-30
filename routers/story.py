from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix='/story',
    tags=['story']
)

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