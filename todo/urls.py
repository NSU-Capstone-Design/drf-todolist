from django.urls import path

from todo.views import *

urlpatterns = [
    path('category/get/', get_category),
    path('category/', add_category),
    path('category/<int:pk>', del_category),
    path('todo/', add_todo),
    path('todo/get/', todo_list)
]
