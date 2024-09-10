from django.urls import path
from main.views import show_main
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', include('main.urls')),
]