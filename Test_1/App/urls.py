from django.contrib import admin
from django.urls import path
from .views import find_value
urlpatterns = [
    path('admin/', admin.site.urls),
    path('value', find_value, name='value')
]
