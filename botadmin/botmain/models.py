from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=55)
    sex = models.CharField(max_length=10)
    about = models.TextField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=55)
    desc = models.CharField(max_length=255, null=True)
    sum = models.IntegerField(null=False)
    sex = models.CharField(max_length=10)
    ages = models.IntegerField(null=False)
    agee = models.IntegerField(null=False)
    tasker_d = models.IntegerField(null=False)
    t_date = models.IntegerField(null=False)
    level = models.CharField(max_length=10)
    status = models.IntegerField(default=1, null=True)
    current_sum = models.IntegerField(default=0, null=True)
    users_count = models.IntegerField(default=0, null=True)
    create_date = models.DateField(default=timezone.now, null=True)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_creator',verbose_name='creator id')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasker', verbose_name="selected user", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    donater_id = models.ManyToManyField(User, verbose_name='donater')
    task_id = models.ManyToManyField(Task, verbose_name='task')
    donate = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Донат'
        verbose_name_plural = 'Донаты'


