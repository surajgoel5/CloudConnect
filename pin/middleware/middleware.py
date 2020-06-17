from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class PinAuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        preAuthUrls=[reverse('pinAuth'),reverse('auth')]
        pinAuthorized=request.session.get("pinAuthorized",False)

        if request.path not in preAuthUrls:
            if not pinAuthorized:
                return HttpResponseRedirect("%s?next=%s" % (reverse('pinAuth'), request.path))