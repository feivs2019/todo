from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.TaskHomeView.as_view(), name= 'home'),
    path('create/', views.TaskCreateView.as_view(), name= 'task_create'),
    path('update/<uuid:pk>/', views.TaskUpdateView.as_view(), name= 'task_update'),
    path('delete/<uuid:pk>/', views.TaskDeleteView.as_view(), name= 'task_delete'),
    path('detail/<uuid:pk>/', views.TaskDetailView.as_view(), name= 'task_detail'),
]
