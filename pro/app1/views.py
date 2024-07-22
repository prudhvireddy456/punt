from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from django.http import request
# Create your views her
from .templates import index1

def index(request):
    if request.method == 'POST':
        k=loader.get_template('index.html')
        print(request.POST.get('transcript'))
        k1=index1.get_audio(request.POST.get('transcript'))
        print(k1)
        con={
            'a':k1,
        }
        return HttpResponse(k.render(con,request))
    else:
        k=loader.get_template('index.html')
        return HttpResponse(k.render({},request))
