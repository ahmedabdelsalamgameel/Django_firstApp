
from django.urls import path 
from staff.views import welcome

urlpatterns = [
    path('welcome/',welcome)
]
