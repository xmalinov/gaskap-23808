from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from news.api.v1 import viewsets

news_router = DefaultRouter()
news_router.register("news", viewsets.NewsViewSet, basename="news")

news_comment_router = routers.NestedSimpleRouter(news_router, r"news", lookup="news")

news_comment_router.register(
    r"news-comments", viewsets.NewsCommentViewSet, basename="news-comments"
)

urlpatterns = [
    path(
        "",
        include(news_router.urls),
    ),
    path(
        "",
        include(news_comment_router.urls),
    ),
]
