"""cut_fruit_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.routes.auth import SignupView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from base.routes.vendor.vendor import VendorViewSet

# Constants
API_VERSION = 'v1'

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')

urlpatterns = [
    path('admin/', admin.site.urls),
]

auth_urlpatterns = [
    path('api/' + API_VERSION + '/signup/', SignupView.as_view(), name='signup'),
    path('api/' + API_VERSION + '/login/', LoginView.as_view(), name='login'),
    path('api/' + API_VERSION + '/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/' + API_VERSION + '/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

api_urlpatterns = [
    path(f'api/{API_VERSION}/', include(router.urls)),
]


urlpatterns += auth_urlpatterns 
urlpatterns += api_urlpatterns
