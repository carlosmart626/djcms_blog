#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.utils import timezone
from unittest.mock import patch, MagicMock

from djcms_blog.models import Blog, BlogTitle, Author, AuthorBio, Post, PostTitle, Tag, TagTitle
from djcms_blog.admin import PostAdmin, PostTitleAdmin, make_published, make_unpublished


class BlogAdminTestCase(TestCase):

    def setUp(self):
        self.admin_site = AdminSite()
        self.post_admin = PostAdmin(Post, self.admin_site)
        self.post_title_admin = PostTitleAdmin(PostTitle, self.admin_site)

        self.default_user = User.objects.create_user('luke', 'luke_skywalker@gmail.com', '123123')
        self.default_user.first_name = 'Luke'
        self.default_user.last_name = 'Skywalker'
        self.default_user.save()

        self.blog = Blog.objects.create(
            title="My Blog",
            slug="my-blog",
            cover="my-blog-cover-image.png",
            block_header="My Blog header tag",
            block_footer="My Blog footer tag",
        )
        self.blog_title_en = BlogTitle.objects.create(
            blog=self.blog,
            language='en',
            title="My Blog",
            description="This is My Blog description",
            meta_title="This is My Blog title meta tag",
            meta_description="This is My Blog description meta tag"
        )
        self.blog_title_es = BlogTitle.objects.create(
            blog=self.blog,
            language='es',
            title="Mi Blog",
            description="Esta es la descripción de Mi Blog",
            meta_title="Esta es la meta tag title de Mi Blog",
            meta_description="Esta es la meta tag desccription de Mi Blog"
        )

        self.author = Author.objects.create(
            user=self.default_user,
            cover="/this/is/cover.png",
            image="/this/is/profile.png",
            slug='luke-skywalker',
            location='Tatooine',
            website='http://jedirules.com',
            facebook_profile='https://facebook.com/luke_skywalker',
            twitter_profile='https://twitter.com/luke_skywalker',
            block_header='This is the block header Luke',
            block_footer='This is the block footer Luke',
        )

        self.author_bio_en = AuthorBio.objects.create(
            author=self.author,
            bio="#Hi! \n I'm developer from Tatooine",
            language='en'
        )
        self.author_bio_es = AuthorBio.objects.create(
            author=self.author,
            bio="#Hola! \n Soy desarrollador y soy de Tatooine",
            language='es'
        )

        self.django_tag = Tag.objects.create(
            blog=self.blog,
            cover="tag/cover.jpg",
            name="django",
            slug="django",
            color="red",
            meta_title="meta title",
            meta_description="meta description"
        )
        self.django_tag_en = TagTitle.objects.create(
            tag=self.django_tag,
            language="en",
            name="django",
            description="",
            meta_title="meta title",
            meta_description="meta description"
        )
        self.django_tag_es = TagTitle.objects.create(
            tag=self.django_tag,
            language="es",
            name="django",
            description="",
            meta_title="meta titulo",
            meta_description="meta descripcion"
        )

        self.luke_first_post = Post.objects.create(
            blog=self.blog,
            title="Luke first post",
            slug="luke-first-post",
            author=self.author
        )
        self.luke_first_post.tags.add(self.django_tag)

        self.luke_first_post_en = PostTitle.objects.create(
            post=self.luke_first_post,
            title="Luke first post",
            language='en',
            description="# Luke first post",
            body="This is the post body",
            meta_title="post meta title",
            meta_description="post meta description",
            published=False,
            is_draft=True,
            created=timezone.now(),
            modified=timezone.now(),
            published_date=timezone.now(),
        )
        self.luke_first_post_en.publish()
        self.luke_first_post_es = PostTitle.objects.create(
            post=self.luke_first_post,
            title="Primer post de Luke",
            language='es',
            description="# Primer post de Luke",
            body="Body del primer post",
            meta_title="post meta title",
            meta_description="post meta description",
            published=False,
            is_draft=True,
            created=timezone.now(),
            modified=timezone.now(),
            published_date=timezone.now(),
        )
        self.luke_first_post_es.publish()

    def test_post_admin(self):
        self.assertEqual(self.post_admin.list_display, ['title', 'is_published', 'blog', 'es', 'en'])

        self.assertTrue(self.post_admin.is_published(self.luke_first_post))

        other_post = Post.objects.create(
            blog=self.blog,
            title="other post",
            slug="other-post",
            author=self.author
        )
        self.assertFalse(self.post_admin.is_published(other_post))

        self.assertEqual(self.post_admin.es(self.luke_first_post),
                         '<a href="/admin/djcms_blog/posttitle/3/" class="button">View ES</a>')
        self.assertEqual(self.post_admin.es(other_post),
                         '<a class="button" href="/admin/djcms_blog/posttitle/add/">Add ES</a>')

    def test_post_title_admin_actions(self):
        queryset = PostTitle.objects.filter(is_draft=True)
        self.assertEqual(queryset.filter(published=True).count(), 2)

        request = MagicMock()

        make_unpublished(self.post_title_admin, request, queryset)
        self.assertEqual(PostTitle.objects.filter(is_draft=True, published=True).count(), 0)

        make_published(self.post_title_admin, request, queryset)
        self.assertEqual(PostTitle.objects.filter(is_draft=True, published=True).count(), 2)

        # Call publish more than one time
        make_published(self.post_title_admin, request, queryset)
        self.assertEqual(PostTitle.objects.filter(is_draft=True, published=True).count(), 2)

    def test_post_title_admin(self):
        request = MagicMock()

        self.assertEqual(self.post_title_admin.list_display, ("title", "is_edited", "post", "language", "published"))

        self.assertEqual(self.post_title_admin.view_on_site(self.luke_first_post_en), "/my-blog/luke-first-post/")
        self.assertFalse(self.post_title_admin.is_edited(self.luke_first_post_en))

        self.luke_first_post_en.title = self.luke_first_post_en.title + " edited"
        self.luke_first_post_en.save()
        self.assertTrue(self.post_title_admin.is_edited(self.luke_first_post_en))

        # Published url
        self.assertEqual(self.post_title_admin.view_on_site(self.luke_first_post_en), "/my-blog/luke-first-post/")

        self.luke_first_post_en.unpublish()

        # Draft url
        self.assertEqual(self.post_title_admin.view_on_site(self.luke_first_post_en), "/draft/my-blog/luke-first-post/")

        self.assertEqual(self.post_title_admin.get_model_perms(request), {})
        self.assertEqual(self.post_title_admin.get_queryset(request).count(), 2)
