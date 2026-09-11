from rest_framework import serializers
from accounts.models import User
from freelancers.models import FreelancerProfile
from clients.models import ClientProfile
from services.models import Service, Category
from projects.models import Project
from reviews.models import Review
from notifications.models import Notification
from reports.models import Report
from messaging.models import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'location', 'is_active', 'date_joined']
        read_only_fields = ['date_joined']


class FreelancerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = FreelancerProfile
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ClientProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    freelancer = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['status', 'created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    freelancer = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['status', 'created_at', 'updated_at', 'completed_at']


class ReviewSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    freelancer = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['created_at', 'resolved_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['created_at']
