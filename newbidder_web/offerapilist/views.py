from django.shortcuts import render, HttpResponse
from offerapilist.models import ThirdPartyOffer
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def offer_list(request):
    """显示offerapi列表页"""
    # 获取排序方式
    sort = request.GET.get('sort', 'default')
    # print(sort)
    sorttype = request.GET.get('sorttype', 2)
    # if Type:
    #     # 1.根据类型获取offerapi
    #     offer_objects = ThirdPartyOffer.objects.get_offers_by_Mobile(limit=100, type=Type, sort=sort, sorttype=sorttype)
    # else:
    # 1.获取全部offerapi
    offer_objects = ThirdPartyOffer.objects.get_offers_by_type(limit=1000, sort=sort, sorttype=sorttype)
    top_offer_objects = ThirdPartyOffer.objects.get_offers_by_Mobile(limit=100, type="Mobile")
    # 2.使用模板文件detail.html
    # for offer in offer_objects:
    #     content = {
    #         'userid': offer["userId"], "offerid": offer["offerId"], "name": offer["name"],
    #         "previewLink": offer["previewLink"], "trackinglink": offer["trackingLink"],
    #         "countrycode": offer["countryCode"], "payoutvalue": offer["payoutValue"], "category": offer["category"],
    #         "carrier": offer["carrier"], "platform": offer["platform"]
    #     }
    #     json_list.append(content)
    # return HttpResponse("Hello")
    print(len(offer_objects))
    # print(type(sorttype))
    # sorttype = 1 if sorttype == 0 else 0
    if sorttype == '1':
        # print("改变")
        sorttype = 0
    else:
        sorttype = 1
    # print(sorttype)
    # redirect('/user/address/')
    return render(request, 'offerapilist/index.html',
                  {"offers": offer_objects, 'sorttype': sorttype, 'sort': sort, "topoffers": top_offer_objects})


def offer_details(request, offerid):
    print(offerid)
    offerdetail = ThirdPartyOffer.objects.get_offers_by_type(offerid=offerid, limit=100)[0]
    return render(request, 'offerapilist/detail.html', {"offerdetail": offerdetail})


def offer_search(request):
    offerid = None
    offername = None
    typename = None
    json_list = []
    print(offername, offerid)
    if request.POST.get('searchValue', '') == '1':
        offerid = request.POST.get('searchContent', None)
    if request.POST.get('searchValue', '') == '2':
        offername = request.POST.get('searchContent', None)
    if request.POST.get('searchValue', '') == '3':
        typename = request.POST.get('searchContent', None)
    print(offerid, offername)
    if offerid is not None or offername is not None:
        offer_objects = ThirdPartyOffer.objects.get_offers_by_type(offerid=offerid, offername=offername, limit=100)
    if typename is not None:
        offer_objects = ThirdPartyOffer.objects.get_offers_by_Mobile(limit=100, type=typename)
    print(len(offer_objects))
    # print(offer_objects[0].offerId)
    for offer in offer_objects:
        content = {
            'userid': offer.userId, "offerid": offer.offerId, "name": offer.name,
            "previewLink": offer.previewLink, "trackinglink": offer.trackingLink,
            "countrycode": offer.countryCode, "payoutvalue": offer.payoutValue, "category": offer.category,
            "carrier": offer.carrier, "platform": offer.platform, "sourcename": offer.sourcename
        }
        json_list.append(content)
    return JsonResponse({'offers': json_list})


def index(request):
    offer_objects = ThirdPartyOffer.objects.get_offers_by_type(limit=100)
    return render(request, 'offerapilist/index.html', {"offers": offer_objects})
    # return HttpResponse("hello")


def hello(request):
    return render(request, 'offerapilist/hello.html', {'dicts': [{"offer": "test"}]})
