from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.authorized import authorize
from todo.models import Category


@api_view(["POST"])
def add_category(request):
    token = request.data.get("token")
    user = authorize(token)
    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    Category.objects.create(title=request.data.get("title"), user=user)
    return Response(data={
        "content": "success",
    })


@api_view(["POST"])
def add_todo(request):
    token = request.data.get("token")
    category = request.data.get("category")
    title = request.data.get("title")
    content = request.data.get("content")
    if not token or not title:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = authorize(token)
    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    user.categories.get(title=category).todos.create(title=title, content=content)
    return Response(data={
        "content": "success",
    })


