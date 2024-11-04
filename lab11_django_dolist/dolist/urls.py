from django.urls import path
from . import views
# . operator means same folder

urlpatterns =[
    #load page of the app will be sent to 'index.html' file
    path("", views.index, name='index'),

    #add new task inot the list
    path('add', views.addTodoItem, name='add'),

    #mark a task as copmleted
    path('copmleted/<todo_id>', views.completedTodo, name = 'completed'),
]