from django.test import TestCase
from .models import Task

class TestTaskManager(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description", due_date="2024-06-30", priority=1)

    def test_create_task(self):
        task = Task.objects.create(title="Another Test Task", description="Another Test Description", due_date="2024-07-30", priority=2)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(task.title, "Another Test Task")

    def test_mark_task_complete(self):
        self.task.mark_as_complete()
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        self.task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_assign_task(self):
        self.task.assign_to("User 1")
        self.assertEqual(self.task.assigned_to, "User 1")

    def test_set_due_date(self):
        self.task.update_details(due_date="2024-07-01")
        self.assertEqual(self.task.due_date, "2024-07-01")

