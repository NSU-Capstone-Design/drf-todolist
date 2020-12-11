from django.urls import path

from todo.views import *

urlpatterns = [
    path('categories/', get_category),
    path('category/', add_category),
    path('category/<int:pk>', del_category),
    path('todo/', addTodo),
    path('todo/get/', todo_list)
]
