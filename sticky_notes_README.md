Sticky Notes App
A web application designed to help users manage their notes efficiently by providing features such as creating, editing, viewing, and deleting notes. This project emphasizes secure authentication and a user-friendly interface, crucial aspects of modern web development.

The Sticky Notes app allows users to:

Register and authenticate securely
Create, edit, view, and delete notes
Manage notes efficiently with a clean and responsive user interface
Learning to build a project like this is important because it covers essential web development skills such as secure authentication, database management, and creating a responsive UI.

Installation
To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/sticky-notes-app.git
cd sticky-notes-app
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:


pip install -r requirements.txt
Apply the migrations:


python manage.py migrate
Create a superuser:


python manage.py createsuperuser
Run the development server:


python manage.py runserver
Usage
After installing and running the development server, you can access the application at http://127.0.0.1:8000/.

Register and Login
Register a new user by clicking on the "Register" link.
Login with your credentials to access the application.
Managing Notes
Home: View a list of all your notes.
New Note: Create a new note by clicking on the "New Note" link.
Edit Note: Edit an existing note by clicking on the edit button next to the note.
Delete Note: Delete a note by clicking on the delete button next to the note.
Screenshots
Home Page:
![](Images/Screenshot%202024-06-30%20221813.png)
![](Images/Screenshot%202024-06-30%20221757.png)

New Note:


Edit Note:


Delete Note:


Credits
Developed by Lehi
