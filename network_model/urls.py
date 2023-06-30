from django.conf.urls.static import static
from django.urls import include, path

from server.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL
from .views import *

urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
    path('reg/', RegView.as_view(), name='reg'),
    path('map/', MapView.as_view(), name='map'),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
