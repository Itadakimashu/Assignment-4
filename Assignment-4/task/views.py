from django.shortcuts import render,redirect

from .forms import TaskForm

from .models import TaskModel

# Create your views here.
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'task/create.html', {'form':form , 'title': 'Create Task'})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html',{'tasks':tasks})

def delete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('show_tasks')

def edit_task(request, id):
    task = TaskModel.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    
    return render(request, 'task/create.html', {'form':form , 'title': 'Edit Task'})

