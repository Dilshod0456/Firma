from django.urls import path
from .views import *

app_name = 'driver'

urlpatterns = [
    path('', home, name="Home"),
    path('lists/', lists, name="Ro\'yxat"),
    path('fikirlar/', fikirlar, name="Fikirlar"),
    path('about/', about, name="Haqida"),
    path('<int:pk>/', single, name="Single"),
    path('<int:pk>/pic', pic, name="Pic"),
    path('creat/', creat, name="Yaratish"),
    path('creatf/', creatf, name="Fikir-yaratish"),
    path('tajriba/', tajriba, name="Labaratoriya"),
    path('lists/<int:pk>/', driver_detail, name="Haydovchi-ma`lumotlari"),
    path('fikirlar/<int:pk>/', fikir_detail, name="Batafsil-fikirlar"),
    path('lists/<int:pk>/update', driver_update, name="Taxrirlash"),
    path('lists/<int:pk>/delete', deleted, name="O\'chirish"),
]
