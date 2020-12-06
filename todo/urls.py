from django.urls import path

from todo.views import *


urlpatterns = [
    path('category/', add_category),
    path('todo/', add_todo)
]