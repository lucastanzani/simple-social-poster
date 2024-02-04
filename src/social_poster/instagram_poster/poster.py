from typing import List

from .model import InstagramMediaId, MediaType
from ..service.instagram_service import post_instagram_single_post, post_instagram_carousel


def post_image(
        image_url: str,
        caption: str = None,
        media_type: MediaType = MediaType.IMAGE
) -> InstagramMediaId:
    if media_type not in [MediaType.IMAGE, MediaType.STORY_IMAGE]:
        raise ValueError("The media type must be a video")
    if media_type == MediaType.STORY_IMAGE and caption is not None:
        raise ValueError("Story Images do not have caption")
    if image_url is None:
        raise ValueError("Image URL is required")
    from ..config.instagram_config import instagram_settings
    return post_instagram_single_post(
        page_id=instagram_settings.meta_instagram_page_id,
        content_url=image_url,
        caption=caption,
        media_type=media_type
    )


def post_video(
        video_url: str,
        caption: str = None,
        upload_waiting_time: int = 30,
        media_type: MediaType = MediaType.REEL
) -> InstagramMediaId:
    if media_type not in [MediaType.STORY_VIDEO, MediaType.REEL]:
        raise ValueError("The media type must be a video")
    if video_url is None:
        raise ValueError("Video URL is required")
    from ..config.instagram_config import instagram_settings
    return post_instagram_single_post(
        page_id=instagram_settings.meta_instagram_page_id,
        content_url=video_url,
        caption=caption,
        media_type=media_type,
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
