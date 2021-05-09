from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'home.html', {'name': 'Astha'})

def add(req):
    res = int(req.POST["txtnum1"]) + int(req.POST["txtnum2"])
    return render(req, 'result.html', {'result': res})