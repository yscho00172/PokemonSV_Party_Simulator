from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('compare/<str:pokemon_num>', views.compare, name='compare'),
    path('pokemon/<str:pokemon_num>', views.pokemon.as_view(), name='pokemon'),
]