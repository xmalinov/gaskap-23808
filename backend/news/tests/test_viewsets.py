import factory
from faker import Factory

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from news.tests.factories import NewsFactory, NewsCommentFactory
from home.api.v1.tests.test_viewsets import AuthenticatedAPITestCase
from users.tests.factories import UserFactory

User = get_user_model()
faker = Factory.create()


class NewsAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.news = NewsFactory()
        self.comment = NewsCommentFactory()

    def test_create_news(self):
        data = {"headline": faker.text(), "description": faker.text()}

        response = self.school_client.post(reverse("news-v1:news-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_news(self):
        response = self.client.get(reverse("news-v1:news-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_news(self):
        response = self.client.get(reverse("news-v1:news-detail", args=(self.news.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_news_comment(self):
        data = {"comment": faker.text()}

        response = self.client.post(
            reverse("news-v1:news-comments-list", args=(self.news.pk,)), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_news_comments(self):
        response = self.client.get(
            reverse("news-v1:news-comments-list", args=(self.news.pk,))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_news_comment(self):
        response = self.client.get(
            reverse(
                "news-v1:news-comments-detail", args=(self.news.pk, self.comment.pk)
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_user_cant_post_news(self):
        data = {"headline": faker.text(), "description": faker.text()}

        response = self.client.post(reverse("news-v1:news-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
