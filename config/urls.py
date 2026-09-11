from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from services.models import Service, Category
from freelancers.models import FreelancerProfile


def home(request):
    featured_services = Service.objects.filter(status=Service.STATUS_APPROVED).select_related('freelancer', 'category').order_by('-created_at')[:8]
    top_freelancers = FreelancerProfile.objects.filter(user__is_active=True, is_approved=True).order_by('-rating')[:6]
    categories = Category.objects.filter(is_active=True)
    recent_services = Service.objects.filter(status=Service.STATUS_APPROVED).order_by('-created_at')[:4]
    return render(request, 'home.html', {
        'featured_services': featured_services,
        'top_freelancers': top_freelancers,
        'categories': categories,
        'recent_services': recent_services,
    })


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    return render(request, 'errors/403.html', status=403)


urlpatterns = [
    path('', home, name='home'),
    path('django-admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('freelancers/', include('freelancers.urls', namespace='freelancers')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('services/', include('services.urls', namespace='services')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('messages/', include('messaging.urls', namespace='messaging')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    # REST API
    path('api/', include('api.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
