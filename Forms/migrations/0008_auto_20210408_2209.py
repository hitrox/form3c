# Generated by Django 3.1.7 on 2021-04-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0007_auto_20210408_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
