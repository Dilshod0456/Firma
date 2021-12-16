from django.urls import path
from .views import *

app_name = 'yonalish'

urlpatterns = [
    path('', YonalishListView.as_view(), name = 'yonalish-list'),
    path('creat-yonalish/', YonalishCreateView.as_view(), name="Yonalish-yaratish"),
    path('<int:pk>/', YonalishDetailView.as_view(), name='yonalish-detail'),
    path('<int:pk>/update_detail', YonalishUpdateView.as_view(), name="yonalish-update"),
    path('<int:pk>/delete', YonalishDeleteView.as_view(), name="yonalish-delete"),
]