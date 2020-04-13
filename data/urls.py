from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new', views.new_data, name="new"),
    path('all_data', views.get_data, name="data"),
    path('day', views.get_day, name="day"),
    path('week', views.get_week, name="week"),
    path('month', views.get_month, name="month"),
    path('year', views.get_year, name="year"),
]