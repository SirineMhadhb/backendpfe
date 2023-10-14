from django.urls import path
from django.views import View
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from . import views
from .api import UserAPI 
from knox import views as knox_views
from django.urls import path, include
from .views import ChangePasswordView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='application')
urlpatterns = router.urls

urlpatterns = [
    path ('User_login' , views.User_login) ,
    path ('api/auth/user' , UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]