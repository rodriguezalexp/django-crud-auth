from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404, render

def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id) # obtener tarea (instancia)
        form = TaskForm(instance=task)
        return render(request ,'task_detail.html', {
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form
            })
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': 'Error updating task'
            })

