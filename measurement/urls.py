from django.urls import path

from measurement.views import SensorsView, SensorView, MeasurementsCreateView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsCreateView.as_view()),
]
