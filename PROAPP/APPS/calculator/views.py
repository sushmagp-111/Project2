from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html',{'name':'sushma'})

def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    val3 = int(request.GET['num3'])
    res = val1 + val2 + val3

    return render(request, 'result.html',{'result':res})
