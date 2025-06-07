from django.urls import path
from django.shortcuts import render


def home(request):
    return render(request,'churras/pages/index.html')


urlpatterns = [
    path('', home),

]
