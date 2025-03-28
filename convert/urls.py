from .views import LengthConvertView, WeightConvertView, TemperatureConvertView
from django.urls import path

urlpatterns = [
    path('length/', LengthConvertView.as_view(), name='length_convert'),
    path('weight/', WeightConvertView.as_view(), name='weight_convert'),
    path('temperature/', TemperatureConvertView.as_view(), name='temperature_convert'),
]