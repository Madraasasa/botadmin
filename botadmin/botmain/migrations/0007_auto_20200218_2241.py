# Generated by Django 3.0.3 on 2020-02-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botmain', '0006_auto_20200218_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='agee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='ages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='sum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='t_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='tasker_d',
            field=models.IntegerField(),
        ),
    ]
