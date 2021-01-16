from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.api.v1.serializers import ThreadSerializer, MessageSerializer
from chat.models import Thread, Message


User = get_user_model()


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "get"]

    def get_queryset(self):
        username = self.request.user.username
        user = get_object_or_404(User, username=username)
        threads = user.threads.all()
        return threads


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    lookup_field = "thread"
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "get"]

    def get_queryset(self):
        username = self.request.user.username
        user = get_object_or_404(User, username=username)
        messages = user.messages.all()
        return messages

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)
