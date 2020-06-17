from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.views.decorators.csrf import requires_csrf_token
from django.middleware.csrf import get_token
from django.core.exceptions import ValidationError

class PinForm(forms.Form):
    pin_value=forms.IntegerField(help_text="Enter Pin:")

    def clean_renewal_date(self):
        data = self.cleaned_data['pin_value']
        if data<=9999 and data >=0:
            return data
        else:
            raise (ValidationError)

@requires_csrf_token
def pinAuth(request):
    get_token(request)
    return render(request,'pinAuth.html')

@requires_csrf_token
def auth(request):
    form=forms.Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pin_sent= str(form.data['pin']).strip()
            #return HttpResponse(pin_sent)
            if pin_sent=='1234':
                request.session["pinAuthorized"]=True
                return HttpResponseRedirect("/" )
            else:
                return HttpResponseRedirect(reverse('pinAuth'))



