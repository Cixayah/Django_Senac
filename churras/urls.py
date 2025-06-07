from django.urls import path
from churras.views import home

# dominio/churras/
urlpatterns = [
    path('', home),

]