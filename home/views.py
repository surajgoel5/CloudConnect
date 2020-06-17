from django.shortcuts import render

# Create your views here.
def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context={
    'str1':'Hello World',
    'str2':'Hi Im making a website',
    'numvis':request.session.get("pinAuthorized", False),


    }

    return render(request,'index.html',context)