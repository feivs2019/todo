from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

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
        urlマップ: 'todo:home'
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
        urlマップ: 'todo:task_create'
        method: GET, POST
==================================================='''
class TaskCreateView(LoginRequiredMixin, BaseView, generic.CreateView):
    namespace = 'task_create'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.form = TaskForm(user=self.request.user.id)


'''===================================================
    TaskUpdateViewクラス
        urlマップ: 'todo:task_update'
        method: GET, POST
==================================================='''
class TaskUpdateView(LoginRequiredMixin, BaseView, generic.UpdateView):
    namespace = 'task_update'
    form = TaskForm()


'''===================================================
    TaskDeleteViewクラス
        urlマップ: 'todo:task_delete'
        method: GET, POST
==================================================='''
class TaskDeleteView(LoginRequiredMixin, BaseView, generic.DeleteView):
    namespace = 'task_delete'
    template_name = 'delete.html'


'''===================================================
    TaskDetailViewクラス
        urlマップ: 'todo:task_detail'
        method: GET
==================================================='''
class TaskDetailView(BaseView, generic.DetailView):
    namespace = 'task_detail'
