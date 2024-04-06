from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.media = SocialMedia("user", "YouTube", 100, "vid")

    def test_initialise(self):

        self.assertEqual("user", self.media._username)
        self.assertEqual("YouTube", self.media._platform)
        self.assertEqual(100, self.media.followers)
        self.assertEqual([], self.media._posts)

    def test_invalid_platform(self):
        with self.assertRaises(ValueError) as ex:
            media = SocialMedia("user", "Telegram", 100, "vid")
        self.assertEqual(str(ex.exception), "Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_invalid_followers(self):
        med = SocialMedia("user", "YouTube", 100, "vid")
        with self.assertRaises(ValueError) as ex:
            med.followers = -1
        self.assertEqual(str(ex.exception), "Followers cannot be negative.")

    def test_create_post(self):
        self.media.create_post("photo123")
        self.assertIn("photo123", self.media._posts[len(self.media._posts)-1].values())
        self.media.create_post("photo12")
        self.assertIn("photo12", self.media._posts[len(self.media._posts) - 1].values())
        self.assertEqual(self.media.create_post("photo1"), "New vid post created by user on YouTube.")

    def test_like_post(self):
        self.media.create_post("photo123")
        self.assertEqual(self.media._posts[0]['likes'], 0)
        self.media.like_post(0)
        self.assertEqual(self.media._posts[0]['likes'], 1)
        self.assertEqual(self.media.like_post(0), "Post liked by user.")
        self.assertEqual(self.media._posts[0]['likes'], 2)
        self.media._posts[0]['likes'] = 10
        self.assertEqual(self.media.like_post(0), "Post has reached the maximum number of likes.")
        self.assertEqual(self.media.like_post(1), "Invalid post index.")

    def test_comment(self):
        self.media.create_post("photo123")
        self.assertEqual(len(self.media._posts[0]['comments']), 0)
        self.media.comment_on_post(0, "Qka snimka!")
        self.assertEqual(self.media._posts[0]['comments'][0]["user"], "user")
        self.assertEqual(self.media._posts[0]['comments'][0]["comment"], "Qka snimka!")
        self.assertEqual(len(self.media._posts[0]['comments']), 1)
        self.assertEqual(self.media.comment_on_post(0, "mnogo gotina snimka"), "Comment added by user on the post.")
        self.assertEqual(self.media.comment_on_post(0, "too-short"), "Comment should be more than 10 characters.")
        with self.assertRaises(IndexError) as ex:
            self.media.comment_on_post(4, "Qka snimka!")
        self.assertEqual(str(ex.exception), "list index out of range")


if __name__ == '__main__':
    main()
