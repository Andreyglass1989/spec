# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from recovery_info.models import TypeDamage, File, OperatingSystem, Device
#from django.shortcuts import render

# Create your views here.

def general ( request ):
    return HttpResponse(u'Через четыре года здесь будет что-нибудь')

def general_all ( request ):
    devlist = Device.objects.all()
    OS_list = OperatingSystem.objects.all()
    type_file_list = File.objects.all()
    trable_list = TypeDamage.objects.all()
    return render_to_response(u'ecommerce.html', locals())
    #return render_to_response(u'recovery-date.html', locals())