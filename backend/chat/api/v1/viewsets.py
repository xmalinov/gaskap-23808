from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.api.v1.serializers import ChatSerializer
from chat.models import Chat
from chat.utils import get_user_contact


class ChatViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Chat.objects.all()
        username = self.request.user.username
        contact = get_user_contact(username)
        queryset = contact.chats.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Chat.objects.all()
        chat = get_object_or_404(queryset, pk=pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
