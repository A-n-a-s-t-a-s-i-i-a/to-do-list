from django.urls import path
from to_do_app.views import (TaskListView,
                             TaskCreateView,
                             TaskUpdateView,
                             TaskDeleteView,
                             TagListView,
                             TagCreateView,
                             TagUpdateView,
                             TagDeleteView,
                             task_complete,
                             task_undo)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/complete/", task_complete, name="task_complete"),
    path("task/<int:pk>/undo/", task_undo, name="task_undo"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "to_do_app"
