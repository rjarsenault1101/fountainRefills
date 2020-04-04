from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Datapoint as dp

def index(request): 
    return render(request, 'pages/index.html')

def new_data(request):
    if request.method == 'POST':
        data = request.POST['datapoint']
        #if data < dp.objects.order_by('-id')[0]['value']:
        datapoint = dp(value=data)
        datapoint.save()
    return redirect('index')