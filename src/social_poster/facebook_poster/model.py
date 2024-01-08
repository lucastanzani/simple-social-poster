from datetime import datetime

from pydantic import BaseModel


class FacebookPostWithImageId(BaseModel):
    post_id: str = None
    id: str


class FacebookPostId(BaseModel):
    id: str


class FacebookVideoId(BaseModel):
    id: str


class FacebookPost(BaseModel):
    id: str
    message: str = None
    created_time: datetime


class FacebookImage(BaseModel):
    id: str
    created_time: datetime = None
    updated_time: datetime = None


class FacebookVideo(BaseModel):
    id: str
    updated_time: datetime = None
    created_time: datetime = None
