
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #This registered the hub url.py here
    path('api/v1/', include('hub.urls')),
]
