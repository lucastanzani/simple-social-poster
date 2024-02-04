import unittest
from unittest import TestCase

import dotenv

import utils


class TestFacebookE2E(TestCase):
    def setUp(self):
        dotenv.load_dotenv(".env.test")
        from src.social_poster import facebook_poster
        self.facebook_poster = facebook_poster
        self.message = utils.get_random_string(10)
        self.image_url = "http://nickelsilver.altervista.org/data/BEST_PLACE_IN_THE_WORLD.png"
        self.video_url = "http://nickelsilver.altervista.org/data/file_example_MOV_1280_1_4MB.mov"
        self.image_urls = [self.image_url, self.image_url]

    def test_post_text(self):
        from src.social_poster.facebook_poster.model import FacebookPostId, FacebookPost
        facebook_post_id = self.facebook_poster.post_text(
            caption=self.message,
        )
        self.assertIsInstance(facebook_post_id, FacebookPostId)
        self.assertIsInstance(facebook_post_id.id, str)
        self.assertIsNotNone(facebook_post_id.id)
        self.assertTrue(len(facebook_post_id.id) > 0)
        post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_id.id))
        self.assertEqual(post.message, self.message)
        self.assertEqual(post.id, facebook_post_id.id)

    def test_post_image_no_caption(self):
        from src.social_poster.facebook_poster.model import FacebookPost, FacebookPostWithImageId, FacebookImage
        facebook_post_with_image_id = self.facebook_poster.post_image(
            caption=None,
            image_url=self.image_url
        )
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

    def test_post_image_caption(self):
        from src.social_poster.facebook_poster.model import FacebookPost, FacebookPostWithImageId, FacebookImage
        facebook_post_with_image_id = self.facebook_poster.post_image(
            caption=self.message,
            image_url=self.image_url
        )
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

    def test_post_carousel_caption(self):
        from src.social_poster.facebook_poster.model import FacebookPost, FacebookPostId
        facebook_post_id = self.facebook_poster.post_carousel(
            caption=self.message,
            image_urls=self.image_urls
        )
        self.assertIsInstance(facebook_post_id, FacebookPostId)
        self.assertIsInstance(facebook_post_id.id, str)
        self.assertIsNotNone(facebook_post_id.id)
        self.assertTrue(len(facebook_post_id.id) > 0)
        post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_id.id))
        self.assertEqual(post.id, facebook_post_id.id)
        self.assertEqual(post.message, self.message)

    def test_post_carousel_no_caption(self):
        from src.social_poster.facebook_poster.model import FacebookPostId, FacebookPost
        facebook_post_id = self.facebook_poster.post_carousel(
            caption=None,
            image_urls=self.image_urls
        )
        self.assertIsInstance(facebook_post_id, FacebookPostId)
        self.assertIsInstance(facebook_post_id.id, str)
        self.assertIsNotNone(facebook_post_id.id)
        self.assertTrue(len(facebook_post_id.id) > 0)
        post = FacebookPost(**utils.get_post_by_id(post_id=facebook_post_id.id))
        self.assertEqual(post.id, facebook_post_id.id)
        self.assertIsNone(post.message)

    def test_post_video_caption(self):
        from src.social_poster.facebook_poster.model import FacebookVideo, FacebookVideoId
        facebook_video_id = self.facebook_poster.post_video(
            caption=self.message,
            video_url=self.video_url
        )
        self.assertIsInstance(facebook_video_id, FacebookVideoId)
        self.assertIsInstance(facebook_video_id.id, str)
        self.assertIsNotNone(facebook_video_id.id)
        self.assertTrue(len(facebook_video_id.id) > 0)
        video = FacebookVideo(**utils.get_video_by_id(video_id=facebook_video_id.id))
        self.assertEqual(video.id, facebook_video_id.id)

    def test_post_video_no_caption(self):
        from src.social_poster.facebook_poster.model import FacebookVideoId, FacebookVideo
        facebook_video_id = self.facebook_poster.post_video(
            caption=None,
            video_url=self.video_url
        )
        self.assertIsInstance(facebook_video_id, FacebookVideoId)
        self.assertIsInstance(facebook_video_id.id, str)
        self.assertIsNotNone(facebook_video_id.id)
        self.assertTrue(len(facebook_video_id.id) > 0)
        video = FacebookVideo(**utils.get_video_by_id(video_id=facebook_video_id.id))
        self.assertEqual(video.id, facebook_video_id.id)

    def test_no_caption_throws_exception(self):
        self.assertRaises(ValueError, self.facebook_poster.post_text, None)

    def test_no_caption_no_image_throws_exception(self):
        self.assertRaises(ValueError, self.facebook_poster.post_image, None, None)


if __name__ == '__main__':
    unittest.main()
