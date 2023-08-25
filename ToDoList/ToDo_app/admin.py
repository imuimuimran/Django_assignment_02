from django.contrib import admin
from ToDo_app.models import TaskModel
# Register your models here.
# admin.site.register(BookStoreModel) 


# when we want to show table in admin panel, just comment the above method and use the below method: 
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription')
    
# admin.site.register(TaskModel, TaskModelAdmin) 