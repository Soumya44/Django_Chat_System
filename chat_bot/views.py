from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message

# Create your views here.


def index(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages':messages})

def create_msg(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        if msg == "":
            return HttpResponse(status=204)
        Message.objects.create(content=request.POST.get('message'))
        return HttpResponseRedirect('ok')


def reset_session(request):
    Message.objects.all().delete()
    return HttpResponseRedirect('ok')



