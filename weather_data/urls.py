from django.urls import path
from . import views

urlpatterns=[
    path('add_weather_data',views.add_weather_data,name='add_weather_data'),
    path('list_weather_data',views.list_weather_data,name='list_weather_data'),
    path('summary_data',views.summary_data,name='summary_data')
]
