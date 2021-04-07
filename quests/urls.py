from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home_view, name='home'),
    path('create', create_view, name='create'),
    path('list', list_view, name='list'),
]
