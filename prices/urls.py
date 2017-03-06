"""spec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.conf.urls.defaults import *
#from django.contrib import admin
from prices import views

import views


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^hello/$' , views.hello),
    #url(r'^hello/dt/(-?\d{1,2})/$' , views.curr_datetime),
	url (r'^generic/$'           , views.generic     ),
    url (r'^cat/$'               , views.categories  ),
    url (r'^tag/$'               , views.tags        ),
    url (r'^goods/$'             , views.goods_all   ),
   # url (r'^cat/([:alpha:][:digit:])/$' , views.goods_all),
    url (r'^cat/([a-zA-A0-9]+)/$', views.goods_by_cat),
    url (r'^tag/([a-zA-A0-9]+)/$', views.goods_by_tag),
    url (r'^good/([a-zA-A0-9]+)/$', views.one_good),
    url (r'^new_tag/$', views.new_tag),
    url (r'^save_tag/$', views.save_tag),
    url (r'^new_good/$', views.new_good),
   # url (r'^save_good/$', views.save_good ),

] 