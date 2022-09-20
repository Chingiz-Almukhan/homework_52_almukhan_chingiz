from django.urls import path

from todoapp.views import index_view, add_view, add

urlpatterns = [
    path('', index_view),
    path('add/', add_view),
    path('add/add_to_list/', add)

]