from datetime import datetime

from pydantic import BaseModel


class FacebookPostWithImageId(BaseModel):
	post_id: str
	id: str


class FacebookPostId(BaseModel):
	id: str


class FacebookPost(BaseModel):
	id: str
	message: str = None
	created_time: datetime


class FacebookImage(BaseModel):
	id: str
	created_time: datetime
