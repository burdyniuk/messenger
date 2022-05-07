from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ChatViewSerializer, MessageViewSerializer, ChatViewPatchSerializer, MessageSendSerializer
from .models import Chat, Message
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('-id')
    serializer_class = ChatViewSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['users', 'name', 'type']

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return ChatViewPatchSerializer
        return self.serializer_class


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageViewSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['from_user']

    # create here an if to verify if method POST (sending message)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MessageSendSerializer
        return self.serializer_class
