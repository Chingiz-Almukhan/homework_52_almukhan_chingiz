from django.shortcuts import render, redirect

from todoapp.models import Todo


def add_view(request):
    return render(request, 'add_task.html', context={'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                                                                  ('ready', 'Сделано')]})


def add(request):
    description = request.POST.get('description')
    status = request.POST.get('status')
    deadline = request.POST.get('deadline')
    article = Todo.objects.create(description=description, status=status, deadline=deadline)
    return redirect('http://127.0.0.1:8000/')
