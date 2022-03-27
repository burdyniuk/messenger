from django.urls import path
from authentification.views import GetUserView, MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView, GetClientView, GetMeUserView
# LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', GetClientView, 'profile')
router.register('user', GetUserView, 'user')




urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', GetMeUserView.as_view(), name='me'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    # path('logout/', LogoutView.as_view(), name='auth_logout'),
    # path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]+router.urls