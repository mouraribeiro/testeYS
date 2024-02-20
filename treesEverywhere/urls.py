from django.contrib.auth import admin
from django.urls import path, include

urlpatterns = [
    path('', include('aplicativos.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
