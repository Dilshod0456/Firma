from django.urls import path
from .views import *

app_name = 'yonalish'

urlpatterns = [
    path('', YonalishListView.as_view(), name = 'yonalish-list'),
    path('creat-yonalish/', YonalishCreateView.as_view(), name="Yonalish-yaratish"),
]