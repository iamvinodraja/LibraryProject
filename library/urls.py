"""
URL configuration for library app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    AuthorViewSet, BookViewSet, MemberViewSet, BorrowRecordViewSet,
    register_user, user_profile
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Authentication endpoints
    path('auth/register/', register_user, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile/', user_profile, name='user_profile'),
]