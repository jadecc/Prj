from django.shortcuts import render,HttpResponse,redirect
from . import models
import time
import json
# Create your views here.

# def index(request):
#     return HttpResponse('Index')

codingType='utf-8'              #字符编码
min=5                           #时间下限
max=55                          #时间上限
def dataInsert(request):
    d = json.loads(request.body.decode(codingType))
    clock = time.strftime("%H-%M-%S")
    minute = int(clock.split("-")[1])
    if minute<=min or minute>=max:
        models.TOldMeasureData.objects.create(**d)
        #print(d)
        #print(clock ,'insert success.')
    return HttpResponse('insert success.')