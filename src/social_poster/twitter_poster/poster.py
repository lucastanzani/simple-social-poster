from .model import TwitterPostId
from ..service.twitter_service import post_twitter_image, post_twitter_simple


def post_text(caption: str) -> TwitterPostId:
    if caption is None:
        raise ValueError("Caption is required")
    return post_twitter_simple(
        caption=caption
    )


def post_image(image_url: str, caption: str = None) -> TwitterPostId:
    if image_url is None:
        raise ValueError("Image URL is required")
    return post_twitter_image(
        image_url=image_url,
        caption=caption
    )
