from rest_framework import serializers
from todo.serializers import TodoSerializer
from todo.models import Todo, Category


class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)

    class Meta:
        model = Category
        fields = ['title', 'created_at', 'user', 'todos']


