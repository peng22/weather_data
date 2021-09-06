from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

from django.core.paginator import Paginator
from statistics import mean
import json
# Create your views here.
def add_weather_data(request):
    form =Weather_Data_form
    if request.method=='POST':
        temperature=request.POST['temperature']
        humidity=request.POST['humidity']
        print(temperature,humidity)
        weather_form=Weather_Data_form(request.POST)
        if weather_form.is_valid():
            weather_data=Weather_Data(temperature=temperature,
                                        humidity=humidity)
            weather_data.save()
            check_summary_data()
        else:
            message='Temperature should be between 19 and 28 and Humidity is between35 and 65'
            context={
                'form':form,
                'message':message
                }
            return render(request,'weather_data/add_weather_data.html',context)

    context={
    'form':form,
    'message':""
    }
    return render(request,'weather_data/add_weather_data.html',context)

def check_summary_data():
    weather_data=Weather_Data.objects.all()
    if len(weather_data)%10==0:
        p = Paginator(weather_data, 10)
        num_pages=p.num_pages
        last_page=p.page(num_pages)
        total_temperature=[]
        total_humidity=[]
        dates=[]
        [(total_temperature.append(item.temperature),
                 total_humidity.append(item.humidity),
                 dates.append(item.date_time)) for item in last_page.object_list]
        avg_temperature=round(mean(total_temperature),2)
        avg_humidity=round(mean(total_humidity),2)
        start_date=dates[0]
        end_date=dates[-1]
        summary=Summary_Data(average_temperature=avg_temperature,
                            averge_humidity=avg_humidity,
                            start_date=start_date,
                            end_date=end_date)
        summary.save()
    print(len(weather_data))
    return True

def list_weather_data(request):
    weather_data=Weather_Data.objects.all()
    weather_data_list=[{'temp':item.temperature,
                        'humidity':item.humidity,
                        'date_time':item.date_time}
                        for item in weather_data ]
    for index,item in  enumerate(weather_data_list):
        if index >0:
            if  weather_data_list[index]['temp'] > weather_data_list[index-1]['temp']:
                item['temp_inc']='True'
            elif weather_data_list[index]['temp'] == weather_data_list[index-1]['temp']:
                item['temp_inc']='Nutral'
            else:
                item['temp_inc']='False'
            if  weather_data_list[index]['humidity'] > weather_data_list[index-1]['humidity']:
                item['humid_inc']='True'
            elif weather_data_list[index]['humidity'] == weather_data_list[index-1]['humidity']:
                item['humid_inc']='Nutral'
            else:
                item['humid_inc']='False'
        else:
            item['temp_inc']='Nutral'
            item['humid_inc']='Nutral'



    context={
    'weather_data_list':weather_data_list,
    }
    return render(request,'weather_data/list_weather_data.html',context)


def summary_data(request):
    Summary_data=Summary_Data.objects.all()
    summary_data_list=[{'avg_temp':item.average_temperature,
                        'avg_humid':item.averge_humidity,
                        'start_date':item.start_date,
                        'end_date':item.end_date
                        }
                        for item in Summary_data ]
    for index,item in  enumerate(summary_data_list):
        if index >0:
            if  summary_data_list[index]['avg_temp'] > summary_data_list[index-1]['avg_temp']:
                item['temp_inc']='True'
            elif summary_data_list[index]['avg_temp'] == summary_data_list[index-1]['avg_temp']:
                item['temp_inc']='Nutral'
            else:
                item['temp_inc']='False'
            if  summary_data_list[index]['avg_humid'] > summary_data_list[index-1]['avg_humid']:
                item['humid_inc']='True'
            elif summary_data_list[index]['avg_humid'] == summary_data_list[index-1]['avg_humid']:
                item['humid_inc']='Nutral'
            else:
                item['humid_inc']='False'
        else:
            item['temp_inc']='Nutral'
            item['humid_inc']='Nutral'



    context={
    'summary_data_list':summary_data_list,
    }
    return render(request,'weather_data/summary.html',context)
