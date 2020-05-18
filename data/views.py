from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Datapoint as dp
from datetime import datetime, timedelta
from django.db.models import Count, Avg, Sum
import json
def index(request): 
    context = {
        'allData': getAllData(),
        'thisWeek': getThisWeek(), 
        'thisMonth': getThisMonth(),
        'totalPoints': dp.objects.all().count(),
        'pointsToday': dp.objects.filter(date=datetime.today().strftime("%Y-%m-%d")).count(),
        'dailyAverage': dailyAverage()
    }
    return render(request, 'pages/index.html', context)

def getAllData():
    data = list(dp.objects.order_by('id').values('timestamp', 'value'))
    print(data)
    return json.dumps(data)

def dailyAverage():
    
    data = list(dp.objects.order_by('date').values('date').annotate(total = Count('date')).values('total'))
    print(data)
    avg = getAverage(data)
    print(avg)
    return avg

def getAverage(data):
    sum = 0
    for element in data:
        sum+=element['total']

    return sum/len(data)

def getThisWeek():
    today = datetime.date(datetime.now())
    week_ago = today - timedelta(days=7)
    data = list(dp.objects.order_by('-id').filter(date__range=[week_ago, today]).values())
    return json.dumps(data)

def getThisMonth(): 
    today=datetime.today()
    month = today.strftime("%Y-%m")
    data = list(dp.objects.order_by('date').filter(timestamp__istartswith=month).values('date').annotate(value = Sum('value')))
    return json.dumps(data)
    pass
def new_data(request):
    if request.method == 'POST':
        # Potential race condition. this method may need to be synchronized in some way.
        previous = 0
        all = list(dp.objects.order_by('-id').all())
        if len(all) > 0: 
            previous = all[0].cumulative
            print(previous)
        cumulative = request.POST['datapoint']
        value = int(cumulative) - previous
        #if data < dp.objects.order_by('-id')[0]['value']:
        timestamp = datetime.now()
        datapoint = dp(timestamp=timestamp, date=datetime.date(timestamp), time=datetime.time(timestamp), value=value, cumulative=cumulative)
        datapoint.save()
    return redirect('index')

def get_data(request): 
    
    return render(request, 'index.html', context)

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
        data = list(dp.objects.order_by('-id').filter(date__range=[week_ago, today]).values())
        return JsonResponse(data, safe=False)

def get_month(request):
    if request.method == 'GET': 
        # YYYY-mm
        month = request.GET['month']
        #print(dp.objects.order_by('date').filter(timestamp__istartswith=month).values('date').annotate(value = Avg('value')).query)
        # Find how much exactly in a day. Diff between the day before. 
        data = list(dp.objects.order_by('date').filter(timestamp__istartswith=month).values('date').annotate(value = Avg('value')))
        return JsonResponse(data, safe=False)

def get_year(request):
    if request.method == 'GET': 
        # YYYY
        year = request.GET['year']
        data = list(dp.objects.order_by('-id').filter(timestamp__istartswith=year).values())
        return JsonResponse(data, safe=False)    
