from rest_framework import serializers

from todo.models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'created_at', 'user', 'id']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'created_at', 'category', 'checked']
