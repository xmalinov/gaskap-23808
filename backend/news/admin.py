from django.contrib import admin

from .models import NewsComment, News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "headline", "description", "created")

    search_fields = ("id", "author__name", "headline")


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "news", "comment", "created")

    search_fields = ("id", "author__name", "news__headline")