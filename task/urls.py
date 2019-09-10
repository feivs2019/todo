from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.TaskHomeView.as_view(), name= 'home'),
    path('create/', views.TaskCreateView.as_view(), name= 'create'),
    path('update/<uuid:pk>/', views.TaskUpdateView.as_view(), name= 'update'),
    path('update_status/', views.update_status, name= 'update_status'),
    path('delete/<uuid:pk>/', views.TaskDeleteView.as_view(), name= 'delete'),
    path('detail/<uuid:pk>/', views.TaskDetailView.as_view(), name= 'detail'),
]
