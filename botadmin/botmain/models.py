from django.db import models
from django.utils import timezone
import datetime
from .send_message import *


class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=55)
    sex = models.CharField(max_length=10)
    about = models.CharField(max_length=255, null=True)
    balance = models.IntegerField(null=False)

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
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_creator', verbose_name='creator id')
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


class Button(models.Model):
    first_button = models.CharField(max_length=55)
    second_button = models.CharField(max_length=55)
    third_button = models.CharField(max_length=55)
    fourth_button = models.CharField(max_length=55)
    fifth_button = models.CharField(max_length=55)
    sixth_button = models.CharField(max_length=55)
    seventh_button = models.CharField(max_length=55)
    eighth_button = models.CharField(max_length=55)

    def __str__(self):
        return self.first_button

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'


class Maker(models.Model):
    task_id = models.ManyToManyField(Task, verbose_name='tasks')
    user_id = models.ManyToManyField(User, verbose_name='makers')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Chat(models.Model):
    telegram_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.telegram_id)

    @property
    def messages(self):
        return Message.objects.filter(telegram_id='120929625').all()


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message_id = models.IntegerField(null=False)
    text = models.TextField(null=False)
    answer = models.TextField(null=True)
    telegram_id = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', verbose_name='chats')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        send_message(self.message_id, self.telegram_id, self.answer)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class FAQ(models.Model):
    text = models.TextField(null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

