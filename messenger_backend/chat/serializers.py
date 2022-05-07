from dataclasses import field
from rest_framework import serializers
from .models import Chat, Message
from django.contrib.auth.models import User
from django.db import transaction

class ChatViewSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = ['id', 'name', 'users', 'chat_picture', 'type', 'messages']


class ChatViewPatchSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = ['id', 'name', 'users', 'chat_picture', 'type', 'messages']
    
    @transaction.atomic
    def update(self, instance, validated_data):
        if 'users' in validated_data:
            users = validated_data.pop('users')[0]
            user = User.objects.get(id=users.id)
            instance.users.add(user)
            instance.save()

        return super().update(instance, validated_data)


# create serializer for sending message
class MessageSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'from_user', 'text', 'time', 'photo', 'file']

    @transaction.atomic
    def create(self, validated_data):
        # if 'chat_id' in validated_data:
        # print("I am here")
        request = self.context['request']
        from_user = validated_data['from_user']
        text = validated_data['text']
        message = Message.objects.create(from_user=from_user, text=text)
        chat = Chat.objects.get(id=request.data.get('chat_id'))
        chat.messages.add(message)
        
        # chat.messages.add(message)
        return message


class MessageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'from_user', 'text', 'time', 'photo', 'file']
    
    # def create(self, validated_data):
    #     if 'chat_id' in validated_data:
    #         requested_chat = validated_data.get('chat_id')
    #         chat = Chat.objects.get(id=requested_chat)
    #         print(chat)
    # def create(self, validated_data):
    #     # if 'chat_id' in validated_data:
    #     print(validated_data['chat_id'])
    #     from_user = validated_data['from_user']
    #     text = validated_data['text']
    #     message = Message.objects.create(from_user=from_user, text=text)
    #     # chat = Chat.objects.get(id=validated_data['chat_id'])
        
    #     # chat.messages.add(message)
    #     return message

