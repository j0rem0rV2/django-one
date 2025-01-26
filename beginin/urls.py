from django.urls import path
from .views.post_view import PostView
from beginin import views

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
