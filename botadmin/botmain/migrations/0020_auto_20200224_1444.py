# Generated by Django 3.0.3 on 2020-02-24 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botmain', '0019_auto_20200223_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        # migrations.AlterField(
        #     model_name='message',
        #     name='telegram_id',
        #     # field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='botmain.Chat', verbose_name='messages'),
        # ),
    ]
