from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        query = Todo(title=title, description=description)
        query.save()
    return render (request,'home.html') 
    



def task(request):
    allTask = Todo.objects.all()
    context = {'tasks':allTask}

    return render (request, 'task.html', context)

    


# Create your views here.
