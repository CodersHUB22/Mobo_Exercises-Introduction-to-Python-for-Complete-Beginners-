from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TodoForm
from .models import Todo


def index(request):
    # show the first 10 todos
    todos = Todo.objects.order_by('id')[:10]
    return render(request, 'index.html', {
        'todos': todos
    })


def todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'todo.html', {
        'todo': todo
    })


def todo_new(request):
    return render(request, 'todo_new.html')


def todo_save(request, todo_id):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        todo_text = form.data['todo_text']

        if todo_id == 0:
            todo = Todo.objects.create(todo_text=todo_text)
            todo.save()

        try:
            todo = Todo.objects.get(pk=todo_id)
            todo.todo_text = todo_text
            todo.save()
        except Todo.DoesNotExist as ex:
            print(ex)

    return HttpResponseRedirect(reverse('todo:index'))


def todo_delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
    except Todo.DoesNotExist as ex:
        print(ex)

    return HttpResponseRedirect(reverse('todo:index'))
