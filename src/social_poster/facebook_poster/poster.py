from typing import List

from .model import FacebookPostWithImageId, FacebookPostId, FacebookVideoId
from ..service.facebook_service import post_facebook_page, post_facebook_page_image, post_facebook_page_video, \
    post_facebook_carousel


def post_text(caption: str) -> FacebookPostId:
    if caption is None:
        raise ValueError("Caption is required")
    from ..config.facebook_config import facebook_settings
    return post_facebook_page(
        page_id=facebook_settings.meta_facebook_page_id,
        caption=caption
    )


def post_image(image_url: str, caption: str = None) -> FacebookPostWithImageId:
    if image_url is None:
        raise ValueError("Image URL is required")
    from ..config.facebook_config import facebook_settings
    return post_facebook_page_image(
        page_id=facebook_settings.meta_facebook_page_id,
        image_url=image_url,
        caption=caption
    )


def post_video(video_url: str, caption: str = None) -> FacebookVideoId:
    if video_url is None:
        raise ValueError("Video URL is required")
    from ..config.facebook_config import facebook_settings
    return post_facebook_page_video(
        page_id=facebook_settings.meta_facebook_page_id,
        video_url=video_url,
        caption=caption
    )


def post_carousel(image_urls: List[str], caption: str = None) -> FacebookPostId:
    if image_urls is None or len(image_urls) == 0:
        raise ValueError("Image URLs should be a list of at least one value")
    from ..config.facebook_config import facebook_settings
    return post_facebook_carousel(
        page_id=facebook_settings.meta_facebook_page_id,
        image_urls=image_urls,
        caption=caption,
    )
