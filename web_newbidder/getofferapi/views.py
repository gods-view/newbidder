from django.shortcuts import render
from utils.testtoken import generate_token, certify_token
# Create your views here.
from django.http import HttpResponse
from getofferapi.models import User, ThirdPartyOffer
from django.conf import settings
import json
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


# , email, password
def gettoken(request):
    # print("用户名", request.POST.get('email'))
    # print("密码", request.POST.get('password'))
    print("获取token")
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('password')
        user = User.objects.get_one_passport(email, password)[0]
        token = generate_token(email + password, expire=600)
        request.session['token'] = token
        print(user.email)
        if user:
            return HttpResponse(json.dumps({'email': email, 'password': password, 'token': token}))
        else:
            return HttpResponse(
                json.dumps({"error": "invalid_client", "error_description": "The client credentials are invalid"}))
    else:
        HttpResponse(json.dumps("use get method"))


def login(request):
    print("验证token")
    email = request.POST.get('email')
    password = request.POST.get('password')
    # email = "chuck@newbidder.com"
    # password = "Ihave2cars$"
    # print(request.session)
    token = request.session.get('token')
    # token = ""
    resule = certify_token(email + password, token)
    print(resule)
    return HttpResponse(resule)


# , email, password, token
def getoffer(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    token = request.GET.get('token')
    result = certify_token(email + password, token)
    if result:
        user_obj = User.objects.get_one_passport(email, password)[0]
        if user_obj:
            userid = user_obj.id
            print(userid)
            response = ''
            result = {}
            print("执行查询")
            str_sql = "select * from ThirdPartyOffer WHERE LENGTH(detail)<20*1024 and userId="+str(userid)
            print(str_sql)
            # offers = ThirdPartyOffer.objects.get_all_object()[21482:21483]
            # offers = ThirdPartyOffer.objects.get_one_objects(offerid=8612, taskid=241)
            offers = ThirdPartyOffer.objects.raw(str_sql)
            # print(type(offers))
            for item in offers:
                result["offerId"] = item.offerId
                result["name"] = item.name
                result["previewLink"] = item.previewLink
                result["trackingLink"] = item.trackingLink
                result["countryCode"] = item.countryCode
                result["payoutValue"] = item.payoutValue
                result["category"] = item.category
                result["carrier"] = item.carrier
                result["platform"] = item.platform
                result["detail"] = item.detail
                response += str(result) + ','
                # result["carrier"] = item.carrier.decode()
                # name = offers[0].name
                # pass
                # print(item.name)
            # return json.dumps(response)
            return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"error": "invalid_client", "error_description": "The client credentials are invalid"}))
