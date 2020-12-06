
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('user.urls')),
    path('api/', include('todo.urls'))
]
