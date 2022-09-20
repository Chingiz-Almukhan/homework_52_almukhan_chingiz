from django.shortcuts import render, redirect

from todoapp.models import Todo


def delete_view(request):
    return render(request, 'delete_page.html')


def delete(request):
    pk = request.POST.get('id')
    articles = Todo.objects.get(pk=pk)
    articles.delete()
    return redirect('http://127.0.0.1:8000/')
