from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

class HomeView(View):
    def get(self, request):
        context = {'tasks': Task.objects.all(), 'form': TaskForm}
        return render(request, 'index.html', context=context)
    def post(self, request):
        task_form = TaskForm(request.POST)
        task_form.save()
        return redirect('home')

class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)
        context = {'task': task, 'form': task_form}
        return render(request, 'detail.html', context=context)
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance=task)
        if 'update' in request.POST:
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        return redirect('home')


