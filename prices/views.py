# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from models import Category, Tag, Good, Unit, Lang


# Create your views here.

def generic (request):
    return HttpResponse(u'Через четыре года здесь будет что-нибудь')

def categories(request):
	catlist=Category.objects.all()
	return render_to_response( u'cath.html', locals())

def tags(request):
	taglist = Tag.objects.all()
	return render_to_response(u'tags.html', locals())

def goods_all(request):
	goodlist = Good.objects.all()
	return render_to_response(u'goods_all.html', locals())

def goods_by_cat( request, cat_slug ):
	try:
		cat = Category.objects.get( slug = cat_slug )
		goodlist = cat.good_set.all()
		return render_to_response(u'goods_cat.html', locals())
	except Category.DoesNotExist:
		raise Http404	

def goods_by_tag( request, tag_slug ):
	try:
		tag = Tag.objects.get( slug = tag_slug )
		goodlist = tag.good_set.all()
		return render_to_response(u'goods_tag.html', locals())
	except Category.DoesNotExist:
		raise Http404	

def one_good( request, gslug ):
	try:
		good = Good.objects.get( slug = gslug )
		tags = good.tags.all()
		langs = good.langs.all()
		return render_to_response(u'one_good.html', locals())
	except Category.DoesNotExist:
		raise Http404	

def new_tag( request ):
	return render_to_response(u'new_tags.html', locals())

def save_tag( request ):
	user_agent = request.META["HTTP_USER_AGENT"]
	tagname = request.GET["tagname"]
	tag = Tag(name = tagname)
	tag.save()
	return render_to_response(u'tag_saved.html', locals())

def new_good(request):
	unitlist = Unit.objects.all().order_by('name')
	catlist = Category.objects.all()
	return render_to_response(u'new_good.html', locals())

#def save_good(request):
#	gname  = request.GET['gname']
#	gprice = frequest.GET['gprice']
#	unit   = Unit.object.get(id=int(request.GET['unit'])
	#cat = Category.objects.get(slug = request.GET['cat'])
	#lang = Lang.objects.get( code = u'rus')
	#tags   = request.GET['tags']
	#good = Good (name = gname, price = gprice, unit = unit, cath = cat )
	#return render_to_response(u'good_saved.html', locals())