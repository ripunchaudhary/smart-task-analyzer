from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("Backend is running ✔")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
]
