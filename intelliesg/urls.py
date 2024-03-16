from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from users.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RegisterView.as_view(),name='register'),
    path('envdata/', include('envdata.urls')),
    path('users/', include('users.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
