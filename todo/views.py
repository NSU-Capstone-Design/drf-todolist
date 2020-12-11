from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.authorized import authorize
from todo.models import Category, Todo
from user.models import User
from todo.serializers import CategorySerializer, TodoSerializer
from core.serializers import TodoListSerializer
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def add_category(request):
    if request.method == 'GET':
        token = request.data.get("token")
        category = Category.objects.filter(user=token)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        token = request.data.get("token")
        user = authorize(token)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        Category.objects.create(title=request.data.get("title"), user=user)
        return Response(data={
            "content": "success",
        }, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def del_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category = CategorySerializer(category)
        return Response(category.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    }, status=status.HTTP_200_OK)


'''------------------LDK------------------------------'''


# 리스트 전체 조회
@api_view(['GET', 'DELETE'])
def todo_list(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        listPK = request.data.get("listPK")
        todo_list = Todo.objects.get(pk=listPK)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 리스트 생성
@api_view(["POST"])
def addTodo(request):
    token = request.data.get("token")
    categoryPK = request.data.get("categoryPK")
    title = request.data.get("title")
    content = request.data.get('content')

    category = Category.objects.get(pk = categoryPK)

    user = authorize(token)
    if not user:
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    if not title and not content:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    elif not title:
        category.todos.create(title = "<Empty_title>", content = content)
        return Response(status = status.HTTP_200_OK)
    elif not content:
        category.todos.create(title = title, content = '')
        return Response(status = status.HTTP_200_OK)

    category.todos.create(title = title, content = content)
    return Response(status = status.HTTP_200_OK)
