from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from TestSite1.settings import PIN


class PinAuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        #return HttpResponse(str(reverse('autoPinAuth',kwargs={'pin_sent':1234})))
        preAuthUrls=[reverse('pinAuth'),reverse('auth'),reverse('autoPinAuth',kwargs={'pin_sent':PIN})]
        pinAuthorized=request.session.get("pinAuthorized",False)

        if request.path not in preAuthUrls:
            if not pinAuthorized:
                return HttpResponseRedirect("%s?next=%s" % (reverse('pinAuth'), request.path))