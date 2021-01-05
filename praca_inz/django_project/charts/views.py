from django.shortcuts import render
from django.http import JsonResponse
from .forms import ExampleForm
from .models import UserInputDate, sensor_mean
from weather_station.models import sensor
import datetime

def calendar(request):
	if request.method == 'POST':
		form = ExampleForm(request.POST)
		if form.is_valid():
			date = UserInputDate(date_from = form.cleaned_data['Date_From'], date_to = form.cleaned_data['Date_To'])
			date.save()
	else:
		form = ExampleForm()
	return render(request, 'charts/calendar.html', {'form': form})

def meanvalues(request):
	queryset = sensor.objects.all()
	user = UserInputDate.objects.last()
	TempMean = 0
	PressMean = 0
	HumiMean = 0
	LoopCounter = 0
	temperatures = []
	pressures = []
	humidities = []
	days = []
	for i in range(1,len(queryset)):
		TempMean += queryset[i-1].temperature
		PressMean += queryset[i-1].pressure
		HumiMean += queryset[i-1].humidity
		LoopCounter += 1
		if queryset[i-1].date.date() != queryset[i].date.date():
			DateMean = queryset[i-1].date.date()
			temperatures.append(round(TempMean/LoopCounter,2))
			pressures.append(round(PressMean / LoopCounter,2))
			humidities.append(round(HumiMean / LoopCounter,2))
			days.append(DateMean)
			TempMean = 0
			PressMean = 0
			HumiMean = 0
			LoopCounter = 0

	user_temperatures = []
	user_pressures = []
	user_humidities = []
	user_days = []


	index_from = days.index(user.date_from)
	index_to = days.index(user.date_to)+1
	for x in range (index_from,index_to):
		user_temperatures.append(temperatures[x])
		user_pressures.append(pressures[x])
		user_humidities.append(humidities[x])
		user_days.append(days[x])


	return JsonResponse(data={
		'temperatures': user_temperatures,
		'humidities': user_humidities,
		'pressures': user_pressures,
		'days': user_days,})










# def charts_json(request):
# 	data = []
# 	labels = []
# 	queryset = UserInputDate.objects.last()
# 	date_from = queryset.date_from
# 	date_to = queryset.date_to


