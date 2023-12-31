import os

import dotenv
from pydantic_settings import BaseSettings

if os.getenv("SOCIAL_POSTER_ENV") in ['DEV', 'LOCAL', 'DEVELOPMENT']:
	env_file = ".env.dev"
else:
	env_file = os.environ.get("SOCIAL_POSTER_ENV_FILE") or ".env"

if env_file is not None:
	dotenv.load_dotenv(dotenv.find_dotenv(env_file), override=False)


class MetaSettings(BaseSettings):
	meta_system_user_secret: str
	meta_api_url: str = "https://graph.facebook.com/v18.0"


class FacebookSettings(BaseSettings):
	meta_settings: MetaSettings = MetaSettings()
	meta_facebook_page_id: str


class InstagramSettings(BaseSettings):
	meta_settings: MetaSettings = MetaSettings()
	meta_instagram_page_id: str


class TwitterSettings(BaseSettings):
	twitter_access_token: str
	twitter_access_token_secret: str
	twitter_api_key: str
	twitter_api_key_secret: str
	twitter_min_media_size: int = 5000000
	twitter_max_media_size: int = 15000000


class Settings(BaseSettings):
	facebook_settings: FacebookSettings = FacebookSettings()
	instagram_settings: InstagramSettings = InstagramSettings()
	twitter_settings: TwitterSettings = TwitterSettings()


settings = Settings()
