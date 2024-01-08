from pydantic_settings import BaseSettings

from .meta_config import MetaSettings


class FacebookSettings(BaseSettings):
	meta_settings: MetaSettings = MetaSettings()
	meta_facebook_page_id: str


facebook_settings = FacebookSettings()
