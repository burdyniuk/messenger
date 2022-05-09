from client.models import Client
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
from .serializers import MyTokenObtainPairSerializer, ChangePasswordSerializer, UpdateUserSerializer, GetClientSerializer, GetUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Go back to application and use this code = {}".format(reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="UniAll Messenger"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@uniall.com",
        # to:
        [reset_password_token.user.email]
    )


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class GetClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = GetClientSerializer

class GetUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserSerializer

class GetMeUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        client = Client.objects.get(user_id=request.user.id)
        content = {
            'id': request.user.id,
            'username': str(request.user.username),
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
            'email': str(request.user.email),
            'profile_picture': "http://127.0.0.1:8000/media/"+str(client.profile_picture),
            'last_online': str(client.last_online),
        }

        return Response(content)
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# class LogoutAllView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         tokens = OutstandingToken.objects.filter(user_id=request.user.id)
#         for token in tokens:
#             t, _ = BlacklistedToken.objects.get_or_create(token=token)

#         return Response(status=status.HTTP_205_RESET_CONTENT)
