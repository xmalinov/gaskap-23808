from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from chat.api.v1.serializers import ThreadSerializer, MessageSerializer
from chat.models import Thread, Message


User = get_user_model()


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
    http_method_names = ["post", "get"]

    def get_queryset(self):
        return self.request.user.threads.all()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ["post", "get"]

    def get_queryset(self, *args, **kwargs):
        thread_id = self.kwargs.get("thread_pk")
        thread = get_object_or_404(Thread, id=thread_id)
        return self.request.user.messages.filter(thread=thread)
