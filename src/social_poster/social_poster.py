from .facebook import poster as facebook_poster
from .instagram import poster as instagram_poster
from .twitter import poster as twitter_poster


def facebook_post(caption: str = None, image_url: str = None):
	if caption is None and image_url is None:
		raise ValueError("Either caption or image_url must have a value for Facebook posts")
	return facebook_poster.post(caption=caption, image_url=image_url)


def instagram_post(caption: str = None, image_url: str = None):
	if image_url is None:
		raise ValueError("image_url must have a value for Instagram posts")
	return instagram_poster.post(caption=caption, image_url=image_url)


def twitter_post(caption: str = None, image_url: str = None):
	if caption is None and image_url is None:
		raise ValueError("Either caption or image_url must have a value for Twitter posts")
	return twitter_poster.post(caption=caption, image_url=image_url)
