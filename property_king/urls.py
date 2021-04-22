from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('accounts.urls')),
    path("dashboard/", include("dashboard.urls")),
    path("properties/", include("properties.urls", namespace='properties')),
    path('admin/', admin.site.urls),
]
