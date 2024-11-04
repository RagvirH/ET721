from django.shortcuts import render, redirect
from . models import todolist
from . form import todolistform
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request,'index.html')
    context = {'todo_tasks': todo_tasks}
    return render(request, 'index.html', context)

@require_POST
def addTodoItem(request):
    form = todolistform(request.POST)
    return redirect('index')