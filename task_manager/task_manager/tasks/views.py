from django.shortcuts import render


from django.shortcuts import render
from .models import Task
from .controllers import TaskController

# View function to display the list of tasks
def display_tasks(request):
    controller = TaskController()  # Create an instance of TaskController
    controller.load_tasks()  # Load tasks from the database
    tasks = controller.tasks  # Get the list of tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Render the task list template with tasks

