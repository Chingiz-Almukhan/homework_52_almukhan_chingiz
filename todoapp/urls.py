from django.urls import path

from todoapp.views.add import add_view, add
from todoapp.views.base import index_view
from todoapp.views.delete import delete_view, delete
from todoapp.views.edit import edit_view, edit, confirm_edit

urlpatterns = [
    path('', index_view),
    path('add/', add_view),
    path("add/add_to_list/", add),
    path('edit/', edit_view),
    path('edit/confirm/', edit),
    path('edit/confirm/edit/', confirm_edit),
    path('delete/', delete_view),
    path('delete/confirm/', delete)
]