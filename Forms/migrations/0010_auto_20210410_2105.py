# Generated by Django 3.1.7 on 2021-04-10 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0009_doctor_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Forms.doctor'),
        ),
        migrations.AddField(
            model_name='income',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Forms.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]