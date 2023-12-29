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
	meta_app_id: str = None
	meta_app_secret: str = None
	meta_system_user_secret: str
	meta_business_account_id: str
	meta_api_url: str = "https://graph.facebook.com/v18.0/"


class FacebookSettings(BaseSettings):
	meta_settings: MetaSettings = MetaSettings()
	meta_facebook_page_id: str


class InstagramSettings(BaseSettings):
	meta_settings: MetaSettings = MetaSettings()
	meta_instagram_page_id: str


class TikTokSettings(BaseSettings):
	pass


class Settings(BaseSettings):
	facebook_settings: FacebookSettings = FacebookSettings()
	instagram_settings: InstagramSettings = InstagramSettings()
	tiktok_settings: TikTokSettings = TikTokSettings()


settings = Settings()
