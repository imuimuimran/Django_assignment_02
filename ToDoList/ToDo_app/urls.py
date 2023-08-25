from django.urls import path

from ToDo_app.views import home, input_tasks, show_tasks, edit_task, delete_task, completed_tasks, complete_task

urlpatterns = [
    path('', home),
    path('input_tasks/', input_tasks, name= 'input_tasks'),
    path('show_tasks/', show_tasks, name= 'show_tasks'),
    path('edit_task/<int:id>', edit_task, name= 'edit_task'),
    path('delete_task/<int:id>', delete_task, name= 'delete_task'),
    path('completed_tasks/', completed_tasks, name='completed_tasks'),
    path('complete_task/<int:id>', complete_task, name='complete_task'), 
]



