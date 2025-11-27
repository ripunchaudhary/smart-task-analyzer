from django.urls import path
from .views import AnalyzeTasks, suggest_tasks

urlpatterns = [
    path("analyze/", AnalyzeTasks.as_view()),
    path("suggest/", suggest_tasks),
]
