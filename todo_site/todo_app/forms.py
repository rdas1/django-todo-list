from django.forms import ModelForm
from .models import Task, Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']
        labels = {
            "description": "Add Task"
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body",]
    def __init__(self, *args, **kwargs):
        task_object = kwargs.pop('task')
        super().__init__(*args, **kwargs)
        self.instance.task = task_object
