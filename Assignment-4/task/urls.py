from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]
