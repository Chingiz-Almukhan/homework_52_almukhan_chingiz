from django.urls import path

from todoapp.views import index_view, add_view, add, edit_view, edit, confirm_edit, delete_view, delete

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