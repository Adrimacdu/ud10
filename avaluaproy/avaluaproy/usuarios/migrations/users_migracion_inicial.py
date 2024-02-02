#9.3.c MIGRACIONES USERS

from django.db import migrations
from django.contrib.auth import get_user_model

def crear_usuario_administrador(apps, schema_editor):
    MyUser = get_user_model()
    MyUser.objects.create_superuser(
        email='admin@admin.com',
        password='admin'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_usuario_administrador),
    ]