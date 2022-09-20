from django.shortcuts import render

from todoapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'main_page.html', context)
