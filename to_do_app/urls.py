from django.urls import path
from to_do_app.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
]

app_name = "to_do_app"