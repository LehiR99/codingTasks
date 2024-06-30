from django.db import models

# Define the Task model
class Task(models.Model):
    # Fields of the Task model
    title = models.CharField(max_length=255)  # Title of the task
    description = models.TextField()  # Description of the task
    due_date = models.DateField()  # Due date of the task
    priority = models.IntegerField()  # Priority of the task
    completed = models.BooleanField(default=False)  # Status of task completion
    assigned_to = models.CharField(max_length=255, null=True, blank=True)  # User to whom the task is assigned

    # Method to mark task as complete
    def mark_as_complete(self):
        self.completed = True
        self.save()

    # Method to update task details
    def update_details(self, title=None, description=None, due_date=None, priority=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority
        self.save()

    # Method to assign task to a user
    def assign_to(self, user):
        self.assigned_to = user
        self.save()
