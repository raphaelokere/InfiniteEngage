from django.contrib import admin  # This imports the Django admin module
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('auth/', include('social_django.urls', namespace='social')),  # Social authentication URLs
]
