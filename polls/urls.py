
from django.urls import path

from . import views

urlpatterns = [
    path('aziz/', views.index, name='index'),
]