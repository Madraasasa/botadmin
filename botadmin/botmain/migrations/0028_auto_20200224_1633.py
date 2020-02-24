# Generated by Django 3.0.3 on 2020-02-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botmain', '0027_auto_20200224_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='telegram_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='botmain.Chat', verbose_name='chats'),
        ),
    ]