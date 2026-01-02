from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from gerenciamento.models import Funcionario

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioCreateView(CreateView):
    template_name = "website/form.html"
    model = Funcionario
    fields = '__all__' 
    success_url = reverse_lazy('website:lista_funcionarios')

class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html' 
    model = Funcionario
    fields = '__all__' 
    success_url = reverse_lazy('website:lista_funcionarios') 

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "website/exclui.html" 
    success_url = reverse_lazy("website:lista_funcionarios")