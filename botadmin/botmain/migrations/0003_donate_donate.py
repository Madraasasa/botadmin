# Generated by Django 3.0.3 on 2020-02-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botmain', '0002_task_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='donate',
            field=models.IntegerField(null=True),
        ),
    ]
