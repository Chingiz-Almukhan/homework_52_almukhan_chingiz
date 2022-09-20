from django.shortcuts import render, redirect

from todoapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'main_page.html', context)


def add_view(request):
    return render(request, 'add_task.html', context={'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                                                                  ('ready', 'Сделано')]})


def add(request):
    description = request.POST.get('description')
    status = request.POST.get('status')
    deadline = request.POST.get('deadline')
    article = Article.objects.create(description=description, status=status, deadline=deadline)
    return redirect('http://127.0.0.1:8000/')


def edit_view(request):
    return render(request, 'edit_page.html')


def edit(request):
    pk = request.POST.get('id')
    articles = Article.objects.get(pk=pk)
    context = {'article': articles}
    return render(request, 'edit_task.html', context)


def confirm_edit(request):
    pk = request.POST.get('id')
    articles = Article.objects.get(pk=pk)
    articles.description = request.POST.get('description')
    articles.status = request.POST.get('status')
    articles.deadline = request.POST.get('deadline')
    articles.save()
    return redirect('http://127.0.0.1:8000/')


def delete_view(request):
    return render(request, 'delete_page.html')


def delete(request):
    pk = request.POST.get('id')
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect('http://127.0.0.1:8000/')
