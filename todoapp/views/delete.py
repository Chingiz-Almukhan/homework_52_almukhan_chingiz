from django.shortcuts import render, redirect

from todoapp.models import Article


def delete_view(request):
    return render(request, 'delete_page.html')


def delete(request):
    pk = request.POST.get('id')
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect('http://127.0.0.1:8000/')
