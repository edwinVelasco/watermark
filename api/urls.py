
from django.urls import path, re_path
from .views import ListDocs, DetailDocs
urlpatterns = [
    path('', ListDocs.as_view(), name='list-docs'),
    path('get/<int:pk>/', DetailDocs.as_view(), name='detail-docs'),
]