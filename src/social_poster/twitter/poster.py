from .model import TwitterPostId
from ..service.twitter_service import post_twitter_image, post_twitter_simple


def post(caption: str, image_url: str) -> TwitterPostId:
	if image_url is None:
		return post_twitter_simple(
			caption=caption
		)

	else:
		return post_twitter_image(
			image_url=image_url,
			caption=caption
		)
