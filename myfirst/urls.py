
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('beginin.urls')),  # Mantém a URL "/home"
    path('admin/', admin.site.urls),
]