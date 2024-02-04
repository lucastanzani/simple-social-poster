from enum import Enum

from pydantic import BaseModel


class InstagramMediaId(BaseModel):
    id: str
    container_id: str


class InstagramMedia(BaseModel):
    id: str
    caption: str = None


class MediaType(Enum):
    IMAGE = 0
    STORY_IMAGE = 1
    REEL = 2
    STORY_VIDEO = 3
    CAROUSEL = 4
    CAROUSEL_ITEM = 5
