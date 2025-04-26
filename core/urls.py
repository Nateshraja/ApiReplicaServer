from django.urls import path
from . import views

urlpatterns = [
    path('api/receive-filing/', views.receive_filing, name='receive_filing'),
]
