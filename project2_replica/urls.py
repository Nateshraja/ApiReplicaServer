from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('replication.urls')),  # 👈 include your replication app's urls
]
