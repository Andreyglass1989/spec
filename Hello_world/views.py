# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
#from django.template.loader import get_template
#from django.template import Template, Context
from django.http import HttpResponse, Http404
import datetime

# Create your views here.
def hello(request):
	return HttpResponse(u'Hello')

def curr_datetime( request, offset ):
	try:
		curdate = datetime.datetime.now()
		offset = int(offset)
		if offset < -12 or offset > 12:	 
			raise Http404
		Delta = datetime.timedelta (hours = offset)
		curdate += Delta
		good = offset > -8 and offset < 8
		#Resp= get_template('cur_date.html')
		#Ctx = Context(locals())
		#Result = Resp.render(Ctx)
		#return HttpResponse(Result)
		return render_to_response('recovery-date.html', locals())
	except ValueError:
		raise Http404


def price(request):
	title = u'Чем Бог послал'
	goods= [
		{'name':u"Котлета по-киевски",
		'price': 10.0,
		'unit':u"шт"},
		{'name':u"Котлета по-московски",
		'price': 9.0,
		'unit':u"шт"},
		{'name':u"Макароны",
		'price': 20.0,
		'unit':u"грамм"},
		{'name':u"компот",
		'price': 1.0,
		'unit':u"ст"},
	]
	#goods = []
	return render_to_response('price_list.html', locals())