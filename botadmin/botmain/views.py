from django.http import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Message, Chat


def select_all(request):

    li = Chat.objects.all()
    # for i in li:
    a = Chat.objects.first()
    print(a)
    a = Message.objects.filter(telegram_id=a.telegram_id).all()
    print(a[0].answer)


    return render(request, 'main.html', {'messages': li})


def select_detail(request, pk):
    li = Message.objects.filter(telegram_id=pk)
    return render(request, 'detail.html', {'messages': li})

    # if request.method == "POST":
    #     return HttpResponse(request)


def update_message(request):
    print(request)
    li = Message.objects.filter(message_id=request.GET.get('mybtn'))
    obj = Message.objects.get(message_id=request.GET.get('mybtn'))
    obj.answer = request.GET.get('new_answer')
    obj.save()
    return redirect('select_detail', pk=obj.telegram_id)

