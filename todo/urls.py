from django.urls import path

from todo.views import *
from user.views import *


urlpatterns = [
    path('', getMyTodoList),
    path('category+/', add_category),
    path('todo+/', addTodo)
]