# Simple Social Poster

A simple library to post on Facebook pages, Instagram business accounts and Twitter.
Supports plain text and images with caption.

## Installation:

Install with pip package manager, using TestPyPI repository:

```
 pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ simple-social-poster --no-cache-dir
```

## Configuration

### Environment Variables:

There are three ways to set up required environment variables:

1. By directly setting them in the calling shell / environment (as with `export VARIABLE=VALUE`)
2. By creating a `.env` file in the root directory
3. By creating a custom .env file (such as `.env.prod`) and setting the environment variable `SOCIAL_POSTER_ENV_FILE` to
   the file name.

For options 2 and 3, the env file will be automatically loaded on the package import, without overriding existing
environment variables.

The required environment variables are the following:

- **Twitter**, supporting OAuth 1.0 for the user that has developer access (no need for twitter login):
    - `TWITTER_API_KEY`: the API key of the Twitter Developer app
    - `TWITTER_API_KEY_SECRET`: the API key secret of the Twitter Developer app
    - `TWITTER_ACCESS_TOKEN`: the user access token for the OAuth 1.0 flow, that is available after completing the User
      authentication settings and choosing "Web App, Automated App or Bot" with Read and Write permission
    - `TWITTER_ACCESS_TOKEN_SECRET`: the user access token secret for the OAuth 1.0 flow, that is available after
      completing the User authentication settings and choosing "Web App, Automated App or Bot" with Read and Write
      permission
- **Facebook**:
    - `META_FACEBOOK_PAGE_ID`: the ID of the page that you want to publish as on its own feed
    - `META_SYSTEM_USER_SECRET`: the **long-lasting** user access token, either from a system user (recommended) or a
      normal user. Both need to be granted admin rights on the page above. If using a normal user access token, it has
      to be renewed manually every two months.
- **Instagram**:
    - `META_INSTAGRAM_PAGE_ID`: the ID of the account that you want to publish as. It must be a business account, linked
      to the Facebook page above.
    - `META_SYSTEM_USER_SECRET`: the **long-lasting** user access token from a user with admin rights on both the page
      and the instagram account. Using a system user is recommended. It can (should) be the same as the facebook one.
- **Optional**:
    - `META_API_URL`: optional, to force a specific version of the API to use, otherwise, leave empty.

Please note that for Meta products a development app has to be created and linked to relevant pages and users.

### Sample Usage:

Import the relevant poster directly:

```python
from social_poster import facebook_poster
from social_poster import instagram_poster
from social_poster import twitter_poster

facebook_poster.post_text(caption="Test Post")
facebook_poster.post_image(caption="Test Post", image_url="http://sample.url")
facebook_poster.post_video(caption="Test Post", video_url="http://sample.url")
facebook_poster.post_carousel(caption="Test Post", image_urls=["http://sample.url", "http://sample.url"])

instagram_poster.post_image(caption="Test Post", image_url="http://sample.url")
instagram_poster.post_video(caption="Test Post", video_url="http://sample.url", upload_waiting_time=30)
instagram_poster.post_carousel(caption="Test Post", image_urls=["http://sample.url", "http://sample.url"])

twitter_poster.post_text(caption="Test Post")
twitter_poster.post_image(caption="Test Post", image_url="http://sample.url")
```

or import and use the required methods:

```python
from social_poster.facebook_poster import post_text

post_text(caption="Test Post")
...
```


