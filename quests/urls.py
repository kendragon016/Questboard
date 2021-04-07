from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home_view, name='home'),
    path('create', create_view, name='create'),
    path('list', list_view, name='list'),
    path('edit_board/<int:pk>', edit_board, name='edit_board'),
    path('edit_quest/<int:pk>', edit_quest, name='edit_quest'),
    path('add/<int:pk>', add_view, name='add'),
    path('board/<str>/<int:pk>', board_view, name='board'),
    path('sign_up/<int:pk>', sign_up, name='sign_up'),
    path('confirm_dibs/<str>/<int:pk>', confirm_dibs, name='confirm_dibs'),
]
