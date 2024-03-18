from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def home(request):
    portfo=Portfolio.objects.all()
    data={
        'portfo':portfo
    }
    return render(request,'index.html',data)
