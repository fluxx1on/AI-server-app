from django.contrib import admin
from django.urls import path, include
from .settings import ADMIN_URL_PATH

urlpatterns = [
    path("", include('network_model.urls')),
    path(ADMIN_URL_PATH, admin.site.urls),
]
