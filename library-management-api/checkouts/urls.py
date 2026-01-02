from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkouts, name='checkouts'),
]