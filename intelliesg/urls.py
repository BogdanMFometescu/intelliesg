from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from users.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('envdata/', include('envdata.urls')),
    path('users/', include('users.urls')),
    path('esgmanager/', include('esgmanager.urls')),
    path('socialdata/', include('socialdata.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
