from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Button
from django.urls import reverse

# Create your views here.
def index(request):
    ids=[1,2,3,4,5]
    context={}
    btnclr=[]
    btntext=[]
    for id in ids:
        btn=(Button.objects.get(id=id))

        if btn.getValue():
            btntext.append('Turn Off')
            btnclr.append('success')

        else:
            btntext.append('Turn On')
            btnclr.append('danger')

    context={'data':zip(ids,btntext, btnclr)}
    return render(request,'index.html',context)

def getButtonVal(request, button_id):
    button=Button.objects.get(id=button_id)
    return HttpResponse(str(button.getValue()))
def getButtonLastEdited(request, button_id):
    button=Button.objects.get(id=button_id)
    return HttpResponse(str(button.getLastEdited()))


def switchButton(request, button_id):
    button = Button.objects.get(id=button_id)
    button.switch()
    button.save()
    return HttpResponseRedirect(reverse('index'))

def turnOnButton(request, button_id):
    button = Button.objects.get(id=button_id)
    button.turnOn()
    button.save()
    return HttpResponse(str(button.getValue()))

def turnOffButton(request, button_id):
    button = Button.objects.get(id=button_id)
    button.turnOff()
    button.save()
    return HttpResponse(str(button.getValue()))