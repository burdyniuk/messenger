from django.urls import path
from rest_framework import routers
from .views import ChatViewSet, MessageViewSet
from .serializers import ChatViewSerializer

router = routers.DefaultRouter()
router.register('chat', ChatViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('chats/', ChatViewViewSet, name='chats'),
    # path('mess', MessageViewSet.get_chat_messages, name='chat_messages'),
    # path('my_chats', ChatViewSerializer.get_chat)
]+router.urls