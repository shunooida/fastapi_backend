from db.models import DbStory
from sqlalchemy.orm.session import Session
from routers.schemas import StoryBase, UserAuth

def create_story_path(request: StoryBase, db: Session, current_user: UserAuth):
    new_story = DbStory(
        story_path = request.story_path,
        user_id = current_user.id
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return