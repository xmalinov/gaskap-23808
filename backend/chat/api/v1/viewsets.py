from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response

from chat.api.v1.serializers import ThreadSerializer
from chat.models import Thread


User = get_user_model()


class ChatViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Thread.objects.all()
        username = self.request.user.username
        user = get_object_or_404(User, username=username)
        queryset = user.threads.all()
        serializer = ThreadSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Thread.objects.all()
        chat = get_object_or_404(queryset, pk=pk)
        serializer = ThreadSerializer(chat)
        return Response(serializer.data)

    def create(self, request):
        serializer = ThreadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
