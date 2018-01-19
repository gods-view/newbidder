from django.conf.urls import url
from offerapilist import views

urlpatterns = [
    url('^offerlist/$', views.offer_list),  # 显示offerlist页面
    url('^details/(?P<offerid>.+)/$', views.offer_details),
    url('^offerlist/(?P<Type>.+)/$', views.offer_list),
    url('^index/$', views.index),
    url('^offersearch/$', views.offer_search),
    url('^$', views.hello)
]
