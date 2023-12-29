from typing import Dict, List

import requests

from ..config import settings
from ..facebook.model import FacebookPostId, FacebookPostWithImageId, FacebookPost
from ..instagram.model import InstagramMediaId


def __get_user_token(social_network: str = 'facebook') -> str:
	return settings.model_dump()[f'{social_network.lower()}_settings']['meta_settings']['meta_system_user_secret']


def __get_api_url(social_network: str = 'facebook') -> str:
	return settings.model_dump()[f'{social_network.lower()}_settings']['meta_settings']['meta_api_url']


def __parse_page_array(data: List[Dict], page_id: str) -> str:
	for page in data:
		if page["id"] == page_id:
			return page['access_token']
	raise IndexError("Cannot find the requested page for the current user set up")


def __create_media_container(page_id: str, image_url: str, caption: str) -> str:
	response = requests.post(
		url=f"{__get_api_url(social_network="instagram")}/{page_id}/media",
		params={
			'access_token': __get_user_token(social_network='instagram')
		},
		data={
			"image_url": image_url,
			"caption": caption
		})
	response.raise_for_status()
	return response.json()['id']


def __publish_media_container(page_id: str, creation_id: str) -> str:
	response = requests.post(
		url=f"{__get_api_url(social_network="instagram")}/{page_id}/media_publish",
		params={
			'access_token': __get_user_token(social_network='instagram')
		},
		data={
			"creation_id": creation_id
		})
	response.raise_for_status()
	return response.json()['id']


def get_facebook_page_token(page_id: str) -> str:
	response = requests.get(
		url=f"{__get_api_url(social_network="facebook")}/me/accounts",
		params={
			'access_token': __get_user_token(social_network='facebook')
		}
	)
	response.raise_for_status()
	return __parse_page_array(data=response.json()['data'], page_id=page_id)


def get_post_by_id(page_id, post_id: str) -> FacebookPost:
	page_token = get_facebook_page_token(
		page_id=page_id,
	)
	response = requests.get(
		url=f"{__get_api_url(social_network="facebook")}/{post_id}",
		params={
			'access_token': page_token
		})
	return response.json()


def post_facebook_page_simple(page_id: str, caption: str) -> FacebookPostId:
	response = requests.post(
		url=f"{__get_api_url(social_network="facebook")}/{page_id}/feed",
		params={
			'access_token': get_facebook_page_token(page_id=page_id)
		},
		data={
			"message": caption
		})
	response.raise_for_status()
	return FacebookPostId(**response.json())


def post_instagram_page(page_id: str, image_url: str, caption: str) -> InstagramMediaId:
	creation_id = __create_media_container(page_id=page_id, image_url=image_url, caption=caption)
	return InstagramMediaId(
		id=__publish_media_container(page_id=page_id, creation_id=creation_id),
		container_id=creation_id
	)


def post_facebook_page_image(page_id: str, image_url: str, caption: str) -> FacebookPostWithImageId:
	response = requests.post(
		url=f"{__get_api_url(social_network="facebook")}/{page_id}/photos",
		params={
			'access_token': get_facebook_page_token(page_id=page_id)
		},
		data={
			"url": image_url,
			"message": caption,
			"published": True
		})
	response.raise_for_status()
	return FacebookPostWithImageId(**response.json())
