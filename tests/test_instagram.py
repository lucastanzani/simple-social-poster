import unittest
from unittest import TestCase

import dotenv

from tests import utils


class TestInstagramE2E(TestCase):
	def setUp(self):
		dotenv.load_dotenv(".env.test")
		import src.social_poster as social_poster
		self.social_poster = social_poster
		self.message = "Test"
		self.image_url = "https://avastai.com/content/en/2023-12-28_cover_1_aries_en.png"

	def test_caption_image(self):
		instagram_media_id = self.social_poster.instagram_post(
			caption=self.message,
			image_url=self.image_url
		)
		from src.social_poster.instagram.model import InstagramMediaId, InstagramMedia
		self.assertIsInstance(instagram_media_id, InstagramMediaId)
		self.assertIsInstance(instagram_media_id.id, str)
		self.assertIsInstance(instagram_media_id.container_id, str)
		self.assertIsNotNone(instagram_media_id.id)
		self.assertIsNotNone(instagram_media_id.container_id)
		self.assertTrue(len(instagram_media_id.id) > 0)
		self.assertTrue(len(instagram_media_id.container_id) > 0)
		media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
		self.assertEqual(instagram_media_id.id, media.id)
		self.assertEqual(self.message, media.caption)

	def test_no_caption_image(self):
		instagram_media_id = self.social_poster.instagram_post(
			caption=None,
			image_url=self.image_url
		)
		from src.social_poster.instagram.model import InstagramMediaId, InstagramMedia
		self.assertIsInstance(instagram_media_id, InstagramMediaId)
		self.assertIsInstance(instagram_media_id.id, str)
		self.assertIsNotNone(instagram_media_id.id)
		self.assertTrue(len(instagram_media_id.id) > 0)
		media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
		self.assertEqual(instagram_media_id.id, media.id)
		self.assertIsNone(media.caption)

	def test_no_caption_no_image_throws_exception(self):
		self.assertRaises(ValueError, self.social_poster.instagram_post, None, None)

	def test_caption_no_image_throws_exception(self):
		self.assertRaises(ValueError, self.social_poster.instagram_post, self.message, None)


if __name__ == '__main__':
	unittest.main()
