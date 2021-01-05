from django.urls import path
from .views import ValueListView
from . import views

urlpatterns = [
	path('', views.home, name="station-home"),
	path('datachart/', views.datachart, name="data-chart"),
]
