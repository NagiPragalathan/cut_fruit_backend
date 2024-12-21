from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from base.routes.vendor.vendor import VendorViewSet
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from base.routes.auth import SignupView, LoginView

# Constants
API_VERSION = 'v1'

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Cut Fruit Backend API",
        default_version='v1',
        description="API documentation for the Cut Fruit backend.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@cutfruit.com"),
        license=openapi.License(name="MIT License"),
        security=[{
            'Bearer': []  # This tells Swagger to use Bearer token authentication
        }]
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Router for VendorViewSet
router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Authentication URL patterns
auth_urlpatterns = [
    path('api/' + API_VERSION + '/signup/', SignupView.as_view(), name='signup'),
    path('api/' + API_VERSION + '/login/', LoginView.as_view(), name='login'),
    path('api/' + API_VERSION + '/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/' + API_VERSION + '/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# API URL patterns
api_urlpatterns = [
    path(f'api/{API_VERSION}/', include(router.urls)),
]

# Swagger UI URL pattern
swagger_url_patterns = [
    path(f'swagger/{API_VERSION}/', schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger-ui'),
]

# Include all URL patterns
urlpatterns += auth_urlpatterns
urlpatterns += api_urlpatterns
urlpatterns += swagger_url_patterns
