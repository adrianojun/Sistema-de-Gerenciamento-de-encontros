from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('agendar_encontro/<int:usuario_id>/', views.agendar_encontro, name='agendar_encontro'),
    path('agendar_encontro/', views.agendar_encontro_sem_usuario, name='agendar_encontro_sem_usuario'),
    path('selecionar_usuario/', views.selecionar_usuario, name='selecionar_usuario'),
    path('listagem_encontros/', views.listagem_encontros, name='listagem_encontros'),
    path('acompanhamento/<int:usuario_id>/', views.acompanhamento, name='acompanhamento'),
    path('usuarios_com_encontros/', views.usuarios_com_encontros, name='usuarios_com_encontros'),
    path('excluir_usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('listagem_agendamento/', views.listagem_simples_encontros, name='listagem_agendamento'), 
    path('excluir_encontro/<int:encontro_id>/', views.excluir_encontro, name='excluir_encontro'), 
]
