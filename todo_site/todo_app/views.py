from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Task, Comment
from .forms import TaskForm, CommentForm
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
        comments = Comment.objects.filter(task_id=task_id)
        comment_form = CommentForm(task=task)
        context = {'task': task, 'task_form': task_form, 'comments': comments, 'comment_form': comment_form}
        return render(request, 'detail.html', context=context)
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance=task)
        comment_form = CommentForm(request.POST, task=task)
        if 'update' in request.POST:
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        elif 'add' in request.POST:
            comment_form.save()
            return redirect('detail', task_id=task_id)
        return redirect('home')


