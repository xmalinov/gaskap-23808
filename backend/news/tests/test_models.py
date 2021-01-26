from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from news.models import News, NewsComment
from news.tests.factories import NewsFactory, NewsCommentFactory
from users.tests.factories import UserFactory


class NewsModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.news = NewsFactory.create(author=self.user)

    def test_news(self):
        self.assertEqual(self.news.pk, 1)
