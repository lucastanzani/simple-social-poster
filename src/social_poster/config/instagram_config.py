from pydantic_settings import BaseSettings

from .meta_config import MetaSettings


class InstagramSettings(BaseSettings):
    meta_settings: MetaSettings = MetaSettings()
    meta_instagram_page_id: str


instagram_settings = InstagramSettings()
