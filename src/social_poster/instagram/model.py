from pydantic import BaseModel


class InstagramMediaId(BaseModel):
	id: str
	container_id: str


class InstagramMedia(BaseModel):
	id: str
	caption: str = None
