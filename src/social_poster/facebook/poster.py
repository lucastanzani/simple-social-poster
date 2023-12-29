from typing import Union

from .model import FacebookPostWithImageId, FacebookPostId
from ..config import settings
from ..service.graph_service import post_facebook_page_simple, post_facebook_page_image


def post(caption: str, image_url: str) -> Union[FacebookPostWithImageId, FacebookPostId]:
	if image_url is None:
		return post_facebook_page_simple(
			page_id=settings.facebook_settings.meta_facebook_page_id,
			caption=caption
		)

	else:
		return post_facebook_page_image(
			page_id=settings.facebook_settings.meta_facebook_page_id,
			image_url=image_url,
			caption=caption
		)
