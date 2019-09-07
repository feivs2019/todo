from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name= 'home'),
    path('create/', views.CreateView.as_view(), name= 'task_create'),
    path('update/<uuid:pk>/', views.UpdateView.as_view(), name= 'task_update'),
    path('delete/<uuid:pk>/', views.DeleteView.as_view(), name= 'task_delete'),
    path('detail/<uuid:pk>/', views.DetailView.as_view(), name= 'task_detail'),
]
