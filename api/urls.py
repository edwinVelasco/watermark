
from django.urls import path, re_path
from .views import ListVideo, DetailVideo
urlpatterns = [
    path('', ListVideo.as_view(), name='lista-video'),
    path('get/<int:pk>/', DetailVideo.as_view(), name='detail-video'),
]