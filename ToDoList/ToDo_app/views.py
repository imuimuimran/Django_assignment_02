from django.shortcuts import render, redirect, get_object_or_404
from ToDo_app.forms import TaskModelForm
from ToDo_app.models import TaskModel
# Create your views here. 

def home(request):
    return render(request, 'input_tasks.html')  


def input_tasks(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)   
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('show_tasks') 
    else:
        form = TaskModelForm()
    return render(request, 'input_tasks.html', {'form': form})


# def show_tasks(request):
#     tasks = TaskModel.objects.all()  
#     print(tasks)
#     return render(request, 'show_tasks.html', {'data' : tasks})

def show_tasks(request):
    incomplete_tasks = TaskModel.objects.filter(is_complete=False)
    return render(request, 'show_tasks.html', {'data': incomplete_tasks})



def edit_task(request, id):   
    tasks = TaskModel.objects.get(pk=id) 
    form = TaskModelForm(instance = tasks)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance = tasks)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'input_tasks.html', {'form' : form})   


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_tasks')  

 
def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_complete=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})

def complete_task(request, id):
    # task = TaskModel.objects.get(pk=id)
    task = get_object_or_404(TaskModel, pk=id)
    task.is_complete = True
    task.save()  
    return redirect('completed_tasks')