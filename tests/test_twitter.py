import unittest
from unittest import TestCase
from utils import get_random_string
import dotenv


class TestTwitterE2E(TestCase):
	def setUp(self):
		dotenv.load_dotenv(".env.test")
		import src.social_poster as social_poster
		self.social_poster = social_poster
		self.message = get_random_string(length=10)
		self.image_url = "https://avastai.com/content/en/2023-12-28_cover_1_aries_en.png"

	def test_caption_no_image(self):
		twitter_post_id = self.social_poster.twitter_post(
			caption=self.message,
			image_url=None
		)
		from src.social_poster.twitter.model import TwitterPostId
		self.assertIsInstance(twitter_post_id, TwitterPostId)
		self.assertIsInstance(twitter_post_id.id, str)
		self.assertIsNotNone(twitter_post_id.id)
		self.assertTrue(len(twitter_post_id.id) > 0)
		self.assertEqual(twitter_post_id.text, self.message)

	def test_no_caption_image(self):
		twitter_post_with_image_id = self.social_poster.twitter_post(
			caption=None,
			image_url=self.image_url
		)
		from src.social_poster.twitter.model import TwitterPostId
		self.assertIsInstance(twitter_post_with_image_id, TwitterPostId)
		self.assertIsInstance(twitter_post_with_image_id.id, str)
		self.assertIsNotNone(twitter_post_with_image_id.id)
		self.assertTrue(len(twitter_post_with_image_id.id) > 0)
		self.assertIsNotNone(twitter_post_with_image_id.text)
		self.assertTrue("https://t.co/" in twitter_post_with_image_id.text)

	def test_caption_image(self):
		twitter_post_with_image_id = self.social_poster.twitter_post(
			caption=self.message,
			image_url=self.image_url
		)
		from src.social_poster.twitter.model import TwitterPostId
		self.assertIsInstance(twitter_post_with_image_id, TwitterPostId)
		self.assertIsInstance(twitter_post_with_image_id.id, str)
		self.assertIsNotNone(twitter_post_with_image_id.id)
		self.assertTrue(len(twitter_post_with_image_id.id) > 0)
		self.assertTrue(
			self.message in twitter_post_with_image_id.text and "https://t.co/" in twitter_post_with_image_id.text
		)

	def test_no_caption_no_image_throws_exception(self):
		self.assertRaises(ValueError, self.social_poster.twitter_post, None, None)

	def test_big_image_throws_exception(self):
		pass


if __name__ == '__main__':
	unittest.main()
