from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
'''===================================================
    BaseViewクラス
        urlマップ: なし
==================================================='''
class BaseView(generic.ListView):
    model = Task
    template_name = 'task.html'
    namespace = ''
    page_title = 'Todo'
    context_object_name     = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['namespace'] = self.namespace
        context['page_title'] = self.page_title
        context['username'] = self.request.user.id or "Guest"
        context['form'] = TaskForm
        return context


'''===================================================
    TaskHomeViewクラス
        urlマップ: 'task:home'
        method: GET
==================================================='''
class TaskHomeView(BaseView, generic.ListView):
    namespace = 'home'
    template_name = 'task/home.html'

    def get_queryset(self):
        order_by = ['status','-created_at','author']
        author = self.request.user.id
        if author:
            queryset = Task.objects.select_related().filter(qfilter).order_by(*order_by)
        else:
            queryset = Task.objects.select_related().order_by(*order_by)
        return queryset



'''===================================================
    TaskCreateViewクラス
        urlマップ: 'task:create'
        method: GET, POST
==================================================='''
# class TaskCreateView(LoginRequiredMixin, BaseView, generic.CreateView):
class TaskCreateView(BaseView, generic.CreateView):
    namespace = 'create'
    form_class = TaskForm
    success_url = reverse_lazy('task:home')

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.form = TaskForm(user=self.request.user.id)


'''===================================================
    TaskUpdateViewクラス
        urlマップ: 'task:update'
        method: GET, POST
==================================================='''
class TaskUpdateView(LoginRequiredMixin, BaseView, generic.UpdateView):
    namespace = 'update'
    form = TaskForm()


'''===================================================
    TaskDeleteViewクラス
        urlマップ: 'task:delete'
        method: GET, POST
==================================================='''
class TaskDeleteView(LoginRequiredMixin, BaseView, generic.DeleteView):
    namespace = 'delete'
    template_name = 'delete.html'


'''===================================================
    TaskDetailViewクラス
        urlマップ: 'task:detail'
        method: GET
==================================================='''
class TaskDetailView(BaseView, generic.DetailView):
    namespace = 'detail'
