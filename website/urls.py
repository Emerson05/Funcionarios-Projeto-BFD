from django.urls import path
from .views import (
    IndexTemplateView, 
    FuncionarioListView, 
    FuncionarioCreateView, 
    FuncionarioUpdateView
)

app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('cadastrar/', FuncionarioCreateView.as_view(), name='cria_funcionario'),
    path('funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    
]





