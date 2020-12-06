from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from user.models import User
from todo.models import Category
from todo.serializers import CategorySerializer, TodoSerializer
from core.serializers import TodoListSerializer


@api_view(['GET'])
def status_check(request):
    """
    서버의 상태를 확인하는 함수입니다.
    """
    return Response({
        "status": "OK"
    }, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(login_id=username)

        if user.password == password:
            c = Category.objects.filter(user=user.login_id)
            category = TodoListSerializer(c, many=True)
            return Response(data={"token": user.login_id,
                                  "myTodoList": category.data
                                  })
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
