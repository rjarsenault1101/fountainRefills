from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Datapoint as dp
from datetime import datetime, timedelta
from django.db.models import Count, Avg
def index(request): 
    context = {
        'data': list(dp.objects.order_by('-id').all().values('value', 'timestamp'))
    }
    return render(request, 'pages/index.html', context)

def new_data(request):
    if request.method == 'POST':
        data = request.POST['datapoint']
        #if data < dp.objects.order_by('-id')[0]['value']:
        timestamp = datetime.now()
        datapoint = dp(timestamp=timestamp, date=datetime.date(timestamp), time=datetime.time(timestamp), value=data)
        datapoint.save()
    return redirect('index')

def get_data(request):
    if request.method == 'GET': 
        # Filter by month/day here? 
        data = list(dp.objects.order_by('-id').all().values())
        return JsonResponse(data, safe=False)

def get_day(request):
    if  request.method == 'GET': 
        # expecting YYYY-mm-dd
        date = datetime.strptime(request.GET['day'], '%Y-%m-%d')

        data = list(dp.objects.order_by('-date').filter(date=date.date()).values())
        return JsonResponse(data, safe=False)

def get_week(request):
    if request.method == 'GET': 
        # if request.GET['date']:
        #     today = request.GET['date']
        # else:
        today = datetime.date(datetime.now())
        week_ago = today - timedelta(days=7)
        print("TEST")
        data = list(dp.objects.order_by('-id').filter(date__range=[week_ago, today]).values())
        print(data)
        return JsonResponse(data, safe=False)

def get_month(request):
    if request.method == 'GET': 
        # YYYY-mm
        month = request.GET['month']
        data = list(dp.objects.order_by('date').filter(timestamp__istartswith=month).values('date').annotate(value = Avg('value')))
        return JsonResponse(data, safe=False)

def get_year(request):
    if request.method == 'GET': 
        # YYYY
        year = request.GET['year']
        data = list(dp.objects.order_by('-id').filter(timestamp__istartswith=year).values())
        return JsonResponse(data, safe=False)    
