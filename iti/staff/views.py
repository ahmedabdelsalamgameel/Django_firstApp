from django.shortcuts import render
from django.http import HttpResponse    
# Create your views here.

def welcome(request):
    return HttpResponse("""
                        <h1 style='color:green;align:center;padding-top:300px;padding-left:350px'>
                        Welcome to First app using Django framework
                        </h1>
                        """)