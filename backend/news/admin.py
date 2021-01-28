from django.contrib import admin

from .models import NewsComment, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "headline", "description", "created")
    search_fields = ("id", "author__name", "author__email", "headline")
    raw_id_fields = ("author", "school")


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "news", "comment", "created")
    search_fields = ("id", "author__name", "author__email", "news__headline")
    raw_id_fields = ("author", "news")
