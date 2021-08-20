from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/todo', views.todo, name='todo'),
    path('todo_new', views.todo_new, name='todo_new'),
    path('<int:todo_id>/todo_save', views.todo_save, name='todo_save'),
    path('<int:todo_id>/todo_delete', views.todo_delete, name='todo_delete'),
]
