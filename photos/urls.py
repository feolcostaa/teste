# photos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rota para a lista/galeria principal de fotos
    path('', views.photo_list, name='photo_list'),
    
    # Rota para os detalhes de uma foto específica
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    
    # Rota para a página "Sobre Nós"
    path('sobre-nos/', views.photo_sobre_nos, name='photo_sobre_nos'),
    
    # Rota para a página de contato
    path('contato/', views.photo_contato, name='photo_contato'),
    
    # Rota para a página de sucesso após o envio do formulário
    path('sucesso/', views.photo_sucesso, name='photo_sucesso'),
]