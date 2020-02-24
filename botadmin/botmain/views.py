from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Message, Chat


def select_all(request):

    li = Chat.objects.all()
    # for i in li:
    a = Chat.objects.first()
    # print(a.messages)
    a = Message.objects.filter(telegram_id=a.telegram_id).all()
    print(a[0].answer)


    return render(request, 'main.html', {'messages': li})


def select_detail(request):
    li = Message.objects.filter(telegram_id='120929625')
    return render(request, 'detail.html', {'messages': li})