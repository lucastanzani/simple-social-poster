from typing import Dict, List, Union

import requests

from ..facebook_poster.model import FacebookPostId, FacebookPostWithImageId, FacebookPost, FacebookVideoId


def __get_user_token() -> str:
    from ..config.facebook_config import facebook_settings
    return facebook_settings.meta_settings.meta_system_user_secret


def __get_api_url() -> str:
    from ..config.facebook_config import facebook_settings
    return facebook_settings.meta_settings.meta_api_url


def __parse_page_array(data: List[Dict], page_id: str) -> str:
    for page in data:
        if page["id"] == page_id:
            return page['access_token']
    raise IndexError("Cannot find the requested page for the current user set up")


def get_facebook_page_token(page_id: str) -> str:
    response = requests.get(
        url=f"{__get_api_url()}/me/accounts",
        params={
            'access_token': __get_user_token()
        }
    )
    response.raise_for_status()
    return __parse_page_array(data=response.json()['data'], page_id=page_id)


def get_post_by_id(page_id, post_id: str) -> FacebookPost:
    page_token = get_facebook_page_token(
        page_id=page_id,
    )
    response = requests.get(
        url=f"{__get_api_url()}/{post_id}",
        params={
            'access_token': page_token
        })
    return response.json()


def post_facebook_page(page_id: str, caption: Union[str, None], attached_media: List[str] = None) -> FacebookPostId:
    data = {"message": caption}
    if attached_media is not None:
        data["attached_media"] = [{"media_fbid": value} for value in attached_media]
    response = requests.post(
        url=f"{__get_api_url()}/{page_id}/feed",
        params={
            'access_token': get_facebook_page_token(page_id=page_id)
        },
        json=data
    )
    response.raise_for_status()
    return FacebookPostId(**response.json())


def post_facebook_page_image(
        page_id: str,
        image_url: str,
        caption: Union[str, None],
        published: bool = True
) -> FacebookPostWithImageId:
    response = requests.post(
        url=f"{__get_api_url()}/{page_id}/photos",
        params={
            'access_token': get_facebook_page_token(page_id=page_id)
        },
        data={
            "url": image_url,
            "message": caption,
            "published": published
        })
    response.raise_for_status()
    return FacebookPostWithImageId(**response.json())


def post_facebook_page_video(page_id: str, video_url: str, caption: Union[str, None],
                             published: bool = True) -> FacebookVideoId:
    response = requests.post(
        url=f"{__get_api_url()}/{page_id}/videos",
        params={
            'access_token': get_facebook_page_token(page_id=page_id)
        },
        data={
            "file_url": video_url,
            "message": caption,
            "published": published
        })
    response.raise_for_status()
    return FacebookVideoId(**response.json())


def post_facebook_carousel(page_id: str, image_urls: List[str], caption: Union[str, None]) -> FacebookPostId:
    children = [
        post_facebook_page_image(
            page_id=page_id,
            image_url=image_url,
            caption=caption,
            published=False
        ).id for image_url in image_urls
    ]
    return post_facebook_page(
        page_id=page_id,
        caption=caption,
        attached_media=children
    )
