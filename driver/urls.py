from django.urls import path
from .views import *

app_name = 'driver'

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('lists/', ListsView.as_view(), name="Ro\'yxat"),
    path('fikirlar/', FikirView.as_view(), name="Fikirlar"),
    path('about/', AboutView.as_view(), name="Haqida"),
    path('<int:pk>/', HomePostView.as_view(), name="Single"),
    path('<int:pk>/pic', PicView.as_view(), name="Pic"),
    path('creat/', DriverCreatView.as_view(), name="Yaratish"),
    path('creatf/', FikirCreatView.as_view(), name="Fikir-yaratish"),
    path('tajriba/', LabaratoriyaView.as_view(), name="Labaratoriya"),
    path('lists/<int:pk>/', DriverDetailView.as_view(), name="Haydovchi-ma`lumotlari"),
    path('fikirlar/<int:pk>/', FikirDetailView.as_view(), name="Batafsil-fikirlar"),
    path('lists/<int:pk>/update', DriverUpdateView.as_view(), name="Taxrirlash"),
    path('lists/<int:pk>/delete', deleted, name="delete"),
]
