from django.shortcuts import render

from todoapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'main_page.html', context)


def add_view(request):
    choices = (('new', 'Новая'), ('in process', 'В процессе'), ('ready', 'Сделано'))

    return render(request, 'add_task.html', context={'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                                                                  ('ready', 'Сделано')]})
