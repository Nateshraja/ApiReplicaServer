from django.urls import path
from . import views

urlpatterns = [
    path('receive-filing/', views.receive_filing, name='receive_filing'),
    path('view-filing-records/', views.view_filing_records, name='view_filing_records'),
]
