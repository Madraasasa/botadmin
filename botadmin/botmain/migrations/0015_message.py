# Generated by Django 3.0.3 on 2020-02-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botmain', '0014_maker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
                ('message_id', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
