from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


def get_last_10_messages(chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return chat.messages.order_by("-created").all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact, created = Contact.objects.get_or_create(user=user)
    return contact


def get_current_chat(chat_id):
    return get_object_or_404(Chat, id=chat_id)


def get_chat_participants(chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return chat.participants.all()