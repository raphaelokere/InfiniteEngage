from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('auth/', include('social_django.urls', namespace='social')),  # Social authentication URLs
]
