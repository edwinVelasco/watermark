
from django.urls import path, re_path
from .views import Docs, DetailDocs, TestToken
urlpatterns = [
    path('', Docs.as_view(), name='list-docs'),
    path('get/<int:pk>/', DetailDocs.as_view(), name='detail-docs'),
    path('test_token/', TestToken.as_view(), name='test-token'),
]