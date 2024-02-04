import time
from typing import List

import requests

from ..config.decorators import all_defined
from ..instagram_poster.model import InstagramMediaId
from ..instagram_poster.model import MediaType


def __get_user_token() -> str:
    from ..config.instagram_config import instagram_settings
    return instagram_settings.meta_settings.meta_system_user_secret


def __get_api_url() -> str:
    from ..config.instagram_config import instagram_settings
    return instagram_settings.meta_settings.meta_api_url


@all_defined("creation_id")
def __get_upload_status(creation_id: str) -> str:
    response = requests.get(
        url=f"{__get_api_url()}/{creation_id}",
        params={
            'access_token': __get_user_token(),
            'fields': 'status_code'
        }
    )
    response.raise_for_status()
    return response.json()['status_code']


@all_defined("media_type", "page_id")
def __create_media_container(
        page_id: str,
        caption: str,
        content_url: str = None,
        media_type: MediaType = MediaType.IMAGE,
        children: List[str] = None,
) -> str:
    data = {
        "caption": caption,
    }
    if media_type == MediaType.REEL:
        data['media_type'] = "REELS"
        data["video_url"] = content_url
    elif media_type == MediaType.STORY_VIDEO:
        data['media_type'] = "STORIES"
        data["video_url"] = content_url
    elif media_type == MediaType.CAROUSEL:
        data['media_type'] = "CAROUSEL"
        data['children'] = children
    elif media_type == MediaType.IMAGE:
        data['image_url'] = content_url
    elif media_type == MediaType.STORY_IMAGE:
        data['media_type'] = "STORIES"
        data["image_url"] = content_url
    elif media_type == MediaType.CAROUSEL_ITEM:
        data['image_url'] = content_url
        data['is_carousel_item'] = True
    response = requests.post(
        url=f"{__get_api_url()}/{page_id}/media",
        params={
            'access_token': __get_user_token()
        },
        json=data
    )
    response.raise_for_status()
    return response.json()['id']


def __publish_media_container(
        page_id: str,
        creation_id: str,
        waiting_time: int = 30,
        media_type: MediaType = MediaType.IMAGE
) -> str:
    if media_type == MediaType.REEL or media_type == MediaType.STORY_VIDEO:
        published = False
        counter = 0
        while not published and counter < 5:
            time.sleep(waiting_time)
            status = __get_upload_status(creation_id=creation_id)
            published = status == 'FINISHED'
            counter += 1
    response = requests.post(
        url=f"{__get_api_url()}/{page_id}/media_publish",
        params={
            'access_token': __get_user_token()
        },
        data={
            "creation_id": creation_id
        })
    response.raise_for_status()
    return response.json()['id']


def post_instagram_single_post(
        page_id: str,
        content_url: str,
        media_type: MediaType = MediaType.IMAGE,
        caption: str = None,
        waiting_time: int = 30
) -> InstagramMediaId:
    creation_id = __create_media_container(page_id=page_id, content_url=content_url, caption=caption,
                                           media_type=media_type)
    return InstagramMediaId(
        id=__publish_media_container(page_id=page_id, creation_id=creation_id, media_type=media_type,
                                     waiting_time=waiting_time),
        container_id=creation_id
    )


def post_instagram_carousel(page_id: str, image_urls: List[str], caption: str) -> InstagramMediaId:
    children = [
        __create_media_container(
            page_id=page_id,
            content_url=image_url,
            caption=caption,
            media_type=MediaType.CAROUSEL_ITEM
        ) for image_url in image_urls
    ]
    creation_id = __create_media_container(page_id=page_id, caption=caption, media_type=MediaType.CAROUSEL, children=children)
    return InstagramMediaId(
        id=__publish_media_container(page_id=page_id, creation_id=creation_id, media_type=MediaType.CAROUSEL),
        container_id=creation_id
    )
