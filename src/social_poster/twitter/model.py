from typing import Dict, Union

from pydantic import BaseModel


class TwitterPostId(BaseModel):
	id: str
	text: str


class TwitterMedia(BaseModel):
	media_id: int
	media_id_string: str
	media_key: str = None
	size: int = None
	expires_after_secs: int = None
	image: Dict[str, Union[str, int]]
