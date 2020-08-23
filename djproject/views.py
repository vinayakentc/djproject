from django.http import HttpResponse
from django.shortcuts import render

def file1(request):
    return render(request,"file1.html")