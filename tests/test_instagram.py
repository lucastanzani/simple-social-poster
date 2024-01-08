import unittest
from unittest import TestCase

import dotenv

from tests import utils


class TestInstagramE2E(TestCase):
    def setUp(self):
        dotenv.load_dotenv(".env.test")
        from src.social_poster import instagram_poster
        self.instagram_poster = instagram_poster
        self.message = utils.get_random_string(10)
        self.image_url = "https://avastai.com/content/en/2023-12-28_cover_1_aries_en.png"
        self.video_url = "http://nickelsilver.altervista.org/data/file_example_MOV_1280_1_4MB.mov"
        self.image_urls = [self.image_url, self.image_url]

    def test_caption_image(self):
        instagram_media_id = self.instagram_poster.post_image(
            caption=self.message,
            image_url=self.image_url
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
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
        instagram_media_id = self.instagram_poster.post_image(
            caption=None,
            image_url=self.image_url
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
        self.assertIsInstance(instagram_media_id, InstagramMediaId)
        self.assertIsInstance(instagram_media_id.id, str)
        self.assertIsNotNone(instagram_media_id.id)
        self.assertTrue(len(instagram_media_id.id) > 0)
        media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
        self.assertEqual(instagram_media_id.id, media.id)
        self.assertIsNone(media.caption)

    def test_caption_carousel(self):
        instagram_media_id = self.instagram_poster.post_carousel(
            caption=self.message,
            image_urls=self.image_urls
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
        self.assertIsInstance(instagram_media_id, InstagramMediaId)
        self.assertIsInstance(instagram_media_id.id, str)
        self.assertIsNotNone(instagram_media_id.id)
        self.assertTrue(len(instagram_media_id.id) > 0)
        media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
        self.assertEqual(instagram_media_id.id, media.id)
        self.assertEqual(self.message, media.caption)

    def test_no_caption_carousel(self):
        instagram_media_id = self.instagram_poster.post_carousel(
            caption=None,
            image_urls=self.image_urls
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
        self.assertIsInstance(instagram_media_id, InstagramMediaId)
        self.assertIsInstance(instagram_media_id.id, str)
        self.assertIsNotNone(instagram_media_id.id)
        self.assertTrue(len(instagram_media_id.id) > 0)
        media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
        self.assertEqual(instagram_media_id.id, media.id)
        self.assertIsNone(media.caption)

    def test_caption_reel(self):
        instagram_media_id = self.instagram_poster.post_video(
            caption=self.message,
            video_url=self.video_url
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
        self.assertIsInstance(instagram_media_id, InstagramMediaId)
        self.assertIsInstance(instagram_media_id.id, str)
        self.assertIsNotNone(instagram_media_id.id)
        self.assertTrue(len(instagram_media_id.id) > 0)
        media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
        self.assertEqual(instagram_media_id.id, media.id)
        self.assertEqual(self.message, media.caption)

    def test_no_caption_reel(self):
        instagram_media_id = self.instagram_poster.post_video(
            caption=None,
            video_url=self.video_url
        )
        from src.social_poster.instagram_poster.model import InstagramMediaId, InstagramMedia
        self.assertIsInstance(instagram_media_id, InstagramMediaId)
        self.assertIsInstance(instagram_media_id.id, str)
        self.assertIsNotNone(instagram_media_id.id)
        self.assertTrue(len(instagram_media_id.id) > 0)
        media = InstagramMedia(**utils.get_instagram_element_by_id(instagram_media_id.id, with_caption=True))
        self.assertEqual(instagram_media_id.id, media.id)
        self.assertIsNone(media.caption)

    def test_no_caption_no_image_throws_exception(self):
        self.assertRaises(ValueError, self.instagram_poster.post_image, caption=None, image_url=None)

    def test_caption_no_image_throws_exception(self):
        self.assertRaises(ValueError, self.instagram_poster.post_image, caption=self.message, image_url=None)

    def test_no_caption_no_video_throws_exception(self):
        self.assertRaises(ValueError, self.instagram_poster.post_video, caption=None, video_url=None)

    def test_caption_no_video_throws_exception(self):
        self.assertRaises(ValueError, self.instagram_poster.post_video, caption=self.message, video_url=None)

    def test_caption_no_images_carousel_throws_exception(self):
        self.assertRaises(ValueError, self.instagram_poster.post_carousel, caption=self.message, image_urls=[])
        self.assertRaises(ValueError, self.instagram_poster.post_carousel, caption=None, image_urls=[])
        self.assertRaises(ValueError, self.instagram_poster.post_carousel, caption=self.message, image_urls=None)
        self.assertRaises(ValueError, self.instagram_poster.post_carousel, caption=None, image_urls=None)


if __name__ == '__main__':
    unittest.main()
