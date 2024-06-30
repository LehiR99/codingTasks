import os
import sys

# Add the parent directory of 'tasks' to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
tasks_dir = os.path.join(current_dir, '..', 'tasks')
sys.path.insert(0, tasks_dir)

from tasks.controllers import TaskController
from tasks.views import TaskView

def main():
    # Specify the path to the JSON file for storing tasks
    file_path = 'data/tasks.json'

    # Initialize the TaskController with the specified file path
    controller = TaskController(file_path)

    # Example interactions
    controller.create_task("Task 1", "Description 1", "2024-06-30", 1)
    controller.create_task("Task 2", "Description 2", "2024-07-15", 2)

    # Retrieve and display tasks
    tasks = controller.get_tasks()
    TaskView.display_tasks(tasks)

if __name__ == "__main__":
    main()
