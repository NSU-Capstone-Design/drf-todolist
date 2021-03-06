from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from user.models import User
from todo.models import Category
from user.serializers import UserSerializer
from todo.serializers import CategorySerializer, TodoSerializer
from core.serializers import TodoListSerializer


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(login_id=username)
        if user.password == password:
            return Response(data={"token": user.login_id})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def getMyTodoList(request):
    token = request.data.get("token")
    c = Category.objects.filter(user=token)
    category = TodoListSerializer(c, many=True)
    return Response(data={
        "myTodoList": category.data
    })


'''----------------------------------------------LDK----------------------------'''


@api_view(['POST'])
def signUp(request):
    userID = request.data.get("id")
    password = request.data.get('password')
    checkpwd = request.data.get('checkpwd')

    if not password or not userID or not checkpwd:
        return Response(data={"response": 1})

    if password != checkpwd:
        return Response(data={"response": 2})
    try:
        User.objects.get(login_id=userID)
        return Response(data={"response": 3})
    except:
        newUser = User(login_id=userID, password=password)
        newUser.save()
        serializer = UserSerializer(newUser)
        return Response(serializer.data, status=status.HTTP_200_OK)
