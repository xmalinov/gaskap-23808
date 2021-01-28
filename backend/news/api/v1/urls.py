from django.urls import path, include

from rest_framework_extensions.routers import ExtendedDefaultRouter

from news.api.v1 import viewsets

router = ExtendedDefaultRouter()

news_router = router.register(r"", viewsets.NewsViewSet, basename="news")

news_comment_router = news_router.register(
    r"comments",
    viewsets.NewsCommentViewSet,
    basename="news-comments",
    parents_query_lookups=["news"],
)

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
]
