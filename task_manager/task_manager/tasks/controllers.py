from .models import Task

# Define the TaskController class
class TaskController:
    def __init__(self):
        self.tasks = []  # List to store tasks

    # Method to load tasks from the database
    def load_tasks(self):
        self.tasks = list(Task.objects.all())

    # Method to save tasks to the database
    def save_tasks(self):
        for task in self.tasks:
            task.save()

    # Method to create a new task
    def create_task(self, title, description, due_date, priority):
        task = Task(title=title, description=description, due_date=due_date, priority=priority)
        task.save()
        self.load_tasks()

    # Method to delete a task by its ID
    def delete_task(self, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        self.load_tasks()

    # Method to mark a task as complete by its ID
    def mark_task_complete(self, task_id):
        task = Task.objects.get(id=task_id)
        task.mark_as_complete()
        self.load_tasks()

    # Method to assign a task to a user by its ID
    def assign_task(self, task_id, user):
        task = Task.objects.get(id=task_id)
        task.assign_to(user)
        self.load_tasks()

    # Method to set the due date for a task by its ID
    def set_due_date(self, task_id, due_date):
        task = Task.objects.get(id=task_id)
        task.update_details(due_date=due_date)
        self.load_tasks()
