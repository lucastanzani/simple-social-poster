from .model import InstagramMediaId
from ..config import settings
from ..service.graph_service import post_instagram_page


def post(caption: str, image_url: str) -> InstagramMediaId:
	return post_instagram_page(
		page_id=settings.instagram_settings.meta_instagram_page_id,
		image_url=image_url,
		caption=caption
	)
