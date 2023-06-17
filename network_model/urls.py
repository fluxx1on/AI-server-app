from django.conf.urls.static import static
from django.urls import include, path

from server.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL
from .views import AuthView, MapView

urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
    path('map/', MapView.as_view(), name='map'),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
