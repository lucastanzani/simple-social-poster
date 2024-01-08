from pydantic_settings import BaseSettings


class TwitterSettings(BaseSettings):
    twitter_access_token: str
    twitter_access_token_secret: str
    twitter_api_key: str
    twitter_api_key_secret: str
    twitter_min_media_size: int = 5000000
    twitter_max_media_size: int = 15000000


twitter_settings = TwitterSettings()
