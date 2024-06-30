from django.db import migrations, models
from django.conf import settings

def set_default_user(apps, schema_editor):
    # Adjust this logic to set a default user or None
    User = apps.get_model(settings.AUTH_USER_MODEL)
    try:
        default_user = User.objects.get(username='default_user')
    except User.DoesNotExist:
        default_user = None

    Note = apps.get_model('notes', 'Note')
    for note in Note.objects.all():
        note.user = default_user
        note.save()

class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_post'),  # Adjust to match your actual previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                default=None,  # Set default value to None or a valid user
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_user, reverse_code=migrations.RunPython.noop),
    ]


