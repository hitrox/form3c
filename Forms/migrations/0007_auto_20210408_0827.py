# Generated by Django 3.1.7 on 2021-04-08 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Forms', '0006_auto_20210327_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
