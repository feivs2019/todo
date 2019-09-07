from django.shortcuts import render
from django.views import generic

# Create your views here.
class HomeView(generic.ListView):
    namespace = 'home'

class CreateView(generic.ListView):
    namespace = 'task_create'

class UpdateView(generic.ListView):
    namespace = 'task_update'

class DeleteView(generic.ListView):
    namespace = 'task_delete'

class DetailView(generic.ListView):
    namespace = 'task_detail'

