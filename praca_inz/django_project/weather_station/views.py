from django.shortcuts import render
from .models import sensor
from django.views.generic import ListView
from django.http import JsonResponse

import sys
import datetime

def home(request):
	data = {
		'values': sensor.objects.last()
	}
	return render(request, 'weather_station/index.html', data)

# def datachart(request):
# 	data=[]
# 	data_string=""
# 	hours_back = 4
# 	samples_per_hour = 4
# 	queryset = sensor.objects.order_by('-id')[:hours_back*4]
# 	for x in range (int((len(queryset))/samples_per_hour)):
# 		TempMean = 0
# 		for value in queryset[samples_per_hour*x:samples_per_hour*x+samples_per_hour]:
# 			TempMean += value.temperature
# 		month_nr = int(queryset[x*4].date.strftime("%m"))
# 		month_name = datetime.datetime.strptime(str(month_nr), "%m")
# 		data_string = queryset[x*4].date.strftime("%d ")+month_name.strftime("%b")+queryset[x*4].date.strftime(", %H.00")
# 		data.append({(data_string):(TempMean/samples_per_hour)})
# 		data_reversed = list(reversed(data))
# 	return JsonResponse(data_reversed,safe=False)

def datachart(request):
	data=[]
	labels=[]
	hours_back = 8
	samples_per_hour = 4
	queryset = sensor.objects.order_by('-id')[:hours_back*4]
	for x in range (int((len(queryset))/samples_per_hour)):
		TempMean = 0
		for value in queryset[samples_per_hour*x:samples_per_hour*x+samples_per_hour]:
			TempMean += value.temperature
		month_nr = int(queryset[x*4].date.strftime("%m"))
		month_name = datetime.datetime.strptime(str(month_nr), "%m")
		data_string = queryset[x*4].date.strftime("%d ")+month_name.strftime("%b")+queryset[x*4].date.strftime(", %H.00")
		TempMean = round(TempMean/samples_per_hour,2)
		data.append(TempMean)
		labels.append(data_string)

	labels.reverse()
	data.reverse()
	return JsonResponse(data={
		'labels' : labels,
		'data' : data,
	})

class ValueListView(ListView):
	model = sensor
	template_name = 'weather_station/home.html'
	context_object_name = 'values'


