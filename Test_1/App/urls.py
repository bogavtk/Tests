from django.contrib import admin
from django.urls import path
from .views import calculate, history_objects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate', calculate, name='calculate'),
    path('result', history_objects, name='result'),
]
