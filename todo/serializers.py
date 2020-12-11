from rest_framework import serializers

from todo.models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'user']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'content', 'created_at', 'category', 'checked']
