from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from driver.views import SigupView


urlpatterns = [
    path('admin/', admin.site.urls, name="Admin"),
    path('', include('driver.urls', namespace='driver')),
    path('yonalish/', include('yonalish.urls', namespace='yonalish')),
    path('signup/', SigupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)