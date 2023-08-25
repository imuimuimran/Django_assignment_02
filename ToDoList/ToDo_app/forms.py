from django import forms
from ToDo_app.models import TaskModel
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        
        
