from django.conf.urls import url
from recovery_info import views

import views


urlpatterns = [
   	url (r'^general/$'            , views.general_all    ),
    #url (r'^cat/$'               , views.categories  ),
   # url (r'^tag/$'               , views.tags        ),
   # url (r'^goods/$'             , views.goods_all   ),
   # url (r'^cat/([:alpha:][:digit:])/$' , views.goods_all),
   # url (r'^cat/([a-zA-A0-9]+)/$', views.goods_by_cat),
    #url (r'^tag/([a-zA-A0-9]+)/$', views.goods_by_tag),
    #url (r'^good/([a-zA-A0-9]+)/$', views.one_good),

]