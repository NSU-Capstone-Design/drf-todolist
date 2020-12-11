from django.urls import path, include

from user.views import *  # views/__init__.py 에서 status_check.py를 모듈로 선언했기에 한번에 가져올 수 있습니다.

urlpatterns = [
    path('', login),
    path('signUp/', signUp),
    path('<pk>/', include('todo.urls'))
]