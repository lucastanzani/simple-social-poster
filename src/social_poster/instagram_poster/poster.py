from typing import List

from .model import InstagramMediaId
from ..config.decorators import all_defined
from ..service.instagram_service import post_instagram_single_post, post_instagram_carousel


def post_image(
        image_url: str,
        caption: str = None
) -> InstagramMediaId:
    if image_url is None:
        raise ValueError("Image URL is required")
    from ..config.instagram_config import instagram_settings
    return post_instagram_single_post(
        page_id=instagram_settings.meta_instagram_page_id,
        content_url=image_url,
        caption=caption,
        is_reel=False
    )


def post_video(
        video_url: str,
        caption: str = None,
        upload_waiting_time: int = 30
) -> InstagramMediaId:
    if video_url is None:
        raise ValueError("Video URL is required")
    from ..config.instagram_config import instagram_settings
    return post_instagram_single_post(
        page_id=instagram_settings.meta_instagram_page_id,
        content_url=video_url,
        caption=caption,
        is_reel=True,
        waiting_time=upload_waiting_time
    )


def post_carousel(
        image_urls: List[str],
        caption: str = None
) -> InstagramMediaId:
    if image_urls is None or len(image_urls) == 0:
        raise ValueError("Image URLs should be a list of at least one value")
    from ..config.instagram_config import instagram_settings
    return post_instagram_carousel(
        page_id=instagram_settings.meta_instagram_page_id,
        image_urls=image_urls,
        caption=caption,
    )
