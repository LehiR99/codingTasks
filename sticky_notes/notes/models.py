# models.py

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

def get_default_user_id():
    try:
        return User.objects.get(username='default_user').id
    except User.DoesNotExist:
        return None


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
