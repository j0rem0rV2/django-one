from django.urls import path

from beginin import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]