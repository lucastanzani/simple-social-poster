import io
from tempfile import NamedTemporaryFile

import requests
from PIL import Image
from tweepy import Client, OAuth1UserHandler, API
from tweepy.models import Media

from ..twitter_poster.model import TwitterPostId, TwitterMedia


def __get_twitter_api_key():
    from ..config.twitter_config import twitter_settings
    return twitter_settings.twitter_api_key


def __get_twitter_api_key_secret():
    from ..config.twitter_config import twitter_settings
    return twitter_settings.twitter_api_key_secret


def __get_twitter_access_token():
    from ..config.twitter_config import twitter_settings
    return twitter_settings.twitter_access_token


def __get_twitter_access_token_secret():
    from ..config.twitter_config import twitter_settings
    return twitter_settings.twitter_access_token_secret


def __get_oauth1_client_v2() -> Client:
    return Client(
        consumer_key=__get_twitter_api_key(),
        consumer_secret=__get_twitter_api_key_secret(),
        access_token=__get_twitter_access_token(),
        access_token_secret=__get_twitter_access_token_secret()
    )


def __get_oauth1_client_v1() -> API:
    auth = OAuth1UserHandler(
        consumer_key=__get_twitter_api_key(),
        consumer_secret=__get_twitter_api_key_secret(),
        access_token=__get_twitter_access_token(),
        access_token_secret=__get_twitter_access_token_secret()
    )
    return API(auth)


def __upload_media(image_url: str) -> Media:
    client = __get_oauth1_client_v1()
    img_data = requests.get(image_url).content
    image = Image.open(io.BytesIO(img_data))
    suffix = next(
        (item for item in ['.png', '.jpg', '.svg', '.gif', '.webp'] if item in image_url),
        '.jpg'
    )
    with NamedTemporaryFile(suffix=suffix, delete_on_close=False) as temp_file:
        image.save(temp_file)
        temp_file.flush()
        temp_file.close()
        if temp_file.name is not None:
            response = client.media_upload(filename=temp_file.name, media_category="tweet_image")
            return response
        else:
            raise ValueError("Could not upload image to twitter_poster")


def post_twitter_simple(caption: str) -> TwitterPostId:
    twitter_client = __get_oauth1_client_v2()
    response = twitter_client.create_tweet(
        text=caption
    )

    return TwitterPostId(**response.data)


def post_twitter_image(image_url: str, caption: str) -> TwitterPostId:
    media_id = TwitterMedia(**__upload_media(image_url=image_url).__dict__)
    twitter_client = __get_oauth1_client_v2()
    response = twitter_client.create_tweet(
        text=caption,
        media_ids=[media_id.media_id_string]
    )
    return TwitterPostId(**response.data)
