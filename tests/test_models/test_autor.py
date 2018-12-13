from django.contrib.auth.models import User
from django.test import TestCase

from djcms_blog.models import Author


class AuthorModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("carlosmart", "me@carlosmart.co")

    def test_create_author(self):
        author = Author.objects.create(
            user=self.user,
            cover="/img/cover.jpg",
            image="/img/image.jpg",
            slug="carlosmart",
            location="Medellín",
            website="http://carlosmart.co",
            facebook_profile="https://facebook.com/carlosmart626",
            twitter_profile="https://twitter.com/carlosmart626",
            block_header="carlosmart header",
            block_footer="carlosmart footer"
        )

        self.assertEqual(str(author), "me@carlosmart.co", author)
