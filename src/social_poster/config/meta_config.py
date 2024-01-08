from pydantic_settings import BaseSettings


class MetaSettings(BaseSettings):
	meta_system_user_secret: str
	meta_api_url: str = "https://graph.facebook.com/v18.0"
