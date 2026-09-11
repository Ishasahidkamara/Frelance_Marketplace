from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User
from freelancers.models import FreelancerProfile
from clients.models import ClientProfile
from services.models import Service, Category
from projects.models import Project
from reviews.models import Review
from notifications.models import Notification
from reports.models import Report
from messaging.models import Message
from .serializers import (
    UserSerializer, FreelancerProfileSerializer, ClientProfileSerializer,
    CategorySerializer, ServiceSerializer, ProjectSerializer,
    ReviewSerializer, NotificationSerializer, ReportSerializer, MessageSerializer
)


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class FreelancerProfileViewSet(viewsets.ModelViewSet):
    queryset = FreelancerProfile.objects.all()
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return FreelancerProfile.objects.filter(user__is_active=True, is_approved=True)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [permissions.AllowAny()]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(status=Service.STATUS_APPROVED)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user, status=Service.STATUS_PENDING)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        service = self.get_object()
        service.status = Service.STATUS_APPROVED
        service.save()
        return Response({'status': 'approved'})

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        service = self.get_object()
        service.status = Service.STATUS_REJECTED
        service.save()
        return Response({'status': 'rejected'})


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return Project.objects.all()
        if user.is_client():
            return Project.objects.filter(client=user)
        return Project.objects.filter(freelancer=user)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        project = self.get_object()
        if project.freelancer != request.user:
            return Response({'error': 'Not authorized'}, status=403)
        project.status = Project.STATUS_ACTIVE
        project.save()
        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        project = self.get_object()
        if project.client != request.user:
            return Response({'error': 'Not authorized'}, status=403)
        project.status = Project.STATUS_COMPLETED
        project.save()
        return Response({'status': 'completed'})


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def mark_all_read(self, request):
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return Response({'status': 'all marked read'})


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            return Report.objects.all()
        return Report.objects.filter(reporter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        from django.db.models import Q
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(receiver=user))

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
