from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Reported
import os
from .forms import *


def index(request):
    return render(request,'index.html')


def find(request):
    return render(request,'find.html')


def report(request):

    return render(request,'Report.html')


def reported(request):
    '''if request.POST.get('name') and request.POST.get('description'):
        report = Reported()
        report.name = request.POST.get('name')
        report.description = request.POST.get('description')
        report.image = request.POST.get('images')
        report.save()
'''
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ReportForm()

    data = Reported.objects.raw(f'select * from home_reported')
    use = {
        "id": data
    }

    return render(request,'Reported.html',use,{'form': form})


def success(request):
    data = Reported.objects.raw(f'select * from home_reported')
    use = {
        "id": data
    }
    return render(request,'Reported.html',use)
