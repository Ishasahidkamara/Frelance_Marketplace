from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('freelancers', views.FreelancerProfileViewSet)
router.register('categories', views.CategoryViewSet)
router.register('services', views.ServiceViewSet)
router.register('projects', views.ProjectViewSet, basename='project')
router.register('reviews', views.ReviewViewSet, basename='review')
router.register('notifications', views.NotificationViewSet, basename='notification')
router.register('reports', views.ReportViewSet, basename='report')
router.register('messages', views.MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls')),
]
