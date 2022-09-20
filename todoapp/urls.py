from django.urls import path

from todoapp.views import index_view, add_view

urlpatterns = [
    path('', index_view),
    path('add/', add_view),

]