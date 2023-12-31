import string
import random
from typing import List, Dict

import requests


def __parse_page_array(data: List[Dict], page_id: str) -> str:
	for page in data:
		if page["id"] == page_id:
			return page['access_token']
	raise IndexError("Cannot find the requested page for the current user set up")


def __get_facebook_page_token(page_id: str, api_url: str, user_token) -> str:
	response = requests.get(
		url=f"{api_url}/me/accounts",
		params={
			'access_token': user_token
		}
	)
	response.raise_for_status()
	return __parse_page_array(data=response.json()['data'], page_id=page_id)


def get_post_by_id(post_id: str) -> Dict[str, str]:
	import src.social_poster.config
	settings = src.social_poster.config.settings
	page_token = __get_facebook_page_token(
		page_id=settings.facebook_settings.meta_facebook_page_id,
		api_url=settings.facebook_settings.meta_settings.meta_api_url,
		user_token=settings.facebook_settings.meta_settings.meta_system_user_secret
	)
	response = requests.get(
		url=f"{settings.facebook_settings.meta_settings.meta_api_url}/{post_id}",
		params={
			'access_token': page_token
		})
	return response.json()


def get_image_by_id(image_id: str) -> Dict[str, str]:
	import src.social_poster.config
	settings = src.social_poster.config.settings
	page_token = __get_facebook_page_token(
		page_id=settings.facebook_settings.meta_facebook_page_id,
		api_url=settings.facebook_settings.meta_settings.meta_api_url,
		user_token=settings.facebook_settings.meta_settings.meta_system_user_secret
	)
	response = requests.get(
		url=f"{settings.facebook_settings.meta_settings.meta_api_url}/{image_id}",
		params={
			'access_token': page_token
		})
	return response.json()


def get_instagram_element_by_id(element_id: str, with_caption: bool) -> Dict[str, str]:
	import src.social_poster.config
	settings = src.social_poster.config.settings
	response = requests.get(
		url=f"{settings.instagram_settings.meta_settings.meta_api_url}/{element_id}{'?fields=caption' if with_caption else ''}",
		params={
			'access_token': settings.instagram_settings.meta_settings.meta_system_user_secret
		})
	return response.json()


def get_random_string(length: int):
	# choose from all lowercase letter
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for _ in range(length))
	return result_str
