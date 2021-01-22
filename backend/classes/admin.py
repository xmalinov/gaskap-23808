from django.contrib import admin

from classes.models import Class, ClassVideo, ClassVideoComment


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["name", "teacher", "start_time", "end_time", "get_days"]
    search_field = ["name", "teacher"]
    raw_id_fields = ["teacher", "students", "days"]

    def get_days(self, obj):
        return ", ".join([day.get_name_display() for day in obj.days.all()])

    get_days.short_description = "Week Days"


@admin.register(ClassVideo)
class ClassVideoAdmin(admin.ModelAdmin):
    list_display = ["name", "uploaded_class", "author"]
    search_field = ["author", "name", "uploaded_class"]
    raw_id_fields = ["author", "uploaded_class"]
    readonly_fields = ["created", "modified"]


@admin.register(ClassVideoComment)
class ClassVideoCommentAdmin(admin.ModelAdmin):
    list_display = ["author", "video"]
    raw_id_fields = ["author", "video"]
    search_field = ["author"]
    readonly_fields = ["created", "modified"]
