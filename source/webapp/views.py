from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TaskForm
from webapp.models import Tasks
from webapp.models import STATUS_CHOICES

def tasks_index_view(request, *args, **kwargs):
    if request.method == 'GET':
        articles = Tasks.objects.all()
        return render(request, 'index.html', context={
            'articles' : articles
        })
    elif request.method == 'POST':
        selected_id = request.POST.getlist('selected_items')
        selected_id = [int(i) for i in selected_id]
        print(selected_id)
        Tasks.objects.filter(id__in=request.POST.getlist('selected_items')).delete()
        return redirect('index')


def tasks_find_view(request, *args, pk):
    article = get_object_or_404(Tasks, pk=pk)
    return render(request, 'article.html', context={
        'article': article
    })

def tasks_delete_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')

def tasks_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html' , context={
            'statuses' : STATUS_CHOICES,
            'form' : form
        })
    elif request.method == 'POST':
        form = TaskForm(data = request.POST)
        if form.is_valid():
            task = Tasks.objects.create(
                description=form.cleaned_data['description'],
                status = form.cleaned_data['status'],
                done_date = form.cleaned_data['done_date'],
                detailed_description = form.cleaned_data['detailed_description'],
            )
            return redirect('task_view', pk = task.pk)
        else:
            return render(request, 'create.html', context={'form':form, 'statuses' :STATUS_CHOICES})

def tasks_update_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'description' : task.description,
            'status' : task.status,
            'done_date' : task.done_date,
            'detailed_description' : task.detailed_description,
        })
        return render(request, 'update.html' , context={
            'statuses' : STATUS_CHOICES,
            'form' : form,
            'task' : task
        })
    elif request.method == 'POST':
        form = TaskForm(data = request.POST)
        if form.is_valid():
            task.description=form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.done_date = form.cleaned_data['done_date']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.save()
            return redirect('task_view', pk = task.pk)
        else:
            return render(request, 'update.html', context={'form':form, 'statuses' :STATUS_CHOICES, 'task' : task})
