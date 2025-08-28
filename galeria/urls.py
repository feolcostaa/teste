# galeria/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- ADICIONE ESTA LINHA
from django.conf.urls.static import static  # <-- ADICIONE ESTA LINHA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/', include('photos.urls')),
]

# Adicione esta condição para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)