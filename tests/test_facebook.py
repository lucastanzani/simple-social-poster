import unittest
from unittest import TestCase

import dotenv

import utils


class TestFacebookE2E(TestCase):
	def setUp(self):
		dotenv.load_dotenv(".env.test")
		import src.social_poster as social_poster
		self.social_poster = social_poster
		self.message = "Test"
		self.image_url = "https://avastai.com/content/en/2023-12-28_cover_1_aries_en.png"

	def test_caption_no_image(self):
		facebook_post_id = self.social_poster.facebook_post(
			caption=self.message,
			image_url=None
		)
		from src.social_poster.facebook.model import FacebookPostId, FacebookPost
		self.assertIsInstance(facebook_post_id, FacebookPostId)
		self.assertIsInstance(facebook_post_id.id, str)
		self.assertIsNotNone(facebook_post_id.id)
		self.assertTrue(len(facebook_post_id.id) > 0)
		post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_id.id))
		self.assertEqual(post.message, self.message)
		self.assertEqual(post.id, facebook_post_id.id)

	def test_no_caption_image(self):
		facebook_post_with_image_id = self.social_poster.facebook_post(
			caption=None,
			image_url=self.image_url
		)
		from src.social_poster.facebook.model import FacebookPostWithImageId, FacebookPost, FacebookImage
		self.assertIsInstance(facebook_post_with_image_id, FacebookPostWithImageId)
		self.assertIsInstance(facebook_post_with_image_id.id, str)
		self.assertIsInstance(facebook_post_with_image_id.post_id, str)
		self.assertIsNotNone(facebook_post_with_image_id.id)
		self.assertIsNotNone(facebook_post_with_image_id.post_id)
		self.assertTrue(len(facebook_post_with_image_id.id) > 0)
		self.assertTrue(len(facebook_post_with_image_id.post_id) > 0)
		post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_with_image_id.post_id))
		self.assertIsNone(post.message)
		self.assertEqual(post.id, facebook_post_with_image_id.post_id)
		image = FacebookImage(**utils.get_image_by_id(image_id=facebook_post_with_image_id.id))
		self.assertEqual(image.id, facebook_post_with_image_id.id)

	def test_caption_image(self):
		facebook_post_with_image_id = self.social_poster.facebook_post(
			caption=self.message,
			image_url=self.image_url
		)
		from src.social_poster.facebook.model import FacebookPostWithImageId, FacebookPost, FacebookImage
		self.assertIsInstance(facebook_post_with_image_id, FacebookPostWithImageId)
		self.assertIsInstance(facebook_post_with_image_id.id, str)
		self.assertIsInstance(facebook_post_with_image_id.post_id, str)
		self.assertIsNotNone(facebook_post_with_image_id.id)
		self.assertIsNotNone(facebook_post_with_image_id.post_id)
		self.assertTrue(len(facebook_post_with_image_id.id) > 0)
		self.assertTrue(len(facebook_post_with_image_id.post_id) > 0)
		post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_with_image_id.post_id))
		self.assertEqual(post.message, self.message)
		self.assertEqual(post.id, facebook_post_with_image_id.post_id)
		image = FacebookImage(**utils.get_image_by_id(image_id=facebook_post_with_image_id.id))
		self.assertEqual(image.id, facebook_post_with_image_id.id)

	def test_no_caption_no_image_throws_exception(self):
		self.assertRaises(ValueError, self.social_poster.facebook_post, None, None)


if __name__ == '__main__':
	unittest.main()
