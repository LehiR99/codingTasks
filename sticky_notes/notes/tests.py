# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm


class NoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note content.',
            user=self.user  # Use 'user' instead of 'author'
        )

    def test_note_creation(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note content.')
        self.assertEqual(note.user, self.user)


class NoteFormTest(TestCase):
    def test_note_form_valid(self):
        form = NoteForm(data={
            'title': 'Valid Title',
            'content': 'Valid Content',
        })
        self.assertTrue(form.is_valid())

    def test_note_form_invalid(self):
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Assuming both fields are required


class NoteViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note content.',
            user=self.user  # Use 'user' instead of 'author'
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('notes:note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        response = self.client.get(reverse('notes:note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_detail.html')
        self.assertEqual(response.context['note'], self.note)

    def test_note_create_view(self):
        response = self.client.get(reverse('notes:note_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_edit_view(self):
        response = self.client.get(reverse('notes:note_edit', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_delete_view(self):
        response = self.client.get(reverse('notes:note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_confirm_delete.html')

