from django.urls import path
from . import views

urlpatterns = [
    # Load main page of the app
    path("", views.index, name='index'),

    # Add new task to the list
    path('add/', views.add_task, name='add'),

    # Mark a task as completed
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),

    # Delete a task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # Delete all completed tasks
    path('delete-completed/', views.delete_all_completed, name='delete_completed'),

    # For compatibility with your existing addTodoItem view (if still needed)
    path('addTodoItem/', views.addTodoItem, name='addTodoItem'),

    # For compatibility with your existing completedTodo view (if still needed)
    path('completed/<int:todo_id>/', views.completedTodo, name='completed'),
]