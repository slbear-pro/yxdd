from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from utils.ddutils import get_access_token, get_userid
from apps.user.models import User
from apps.jixiao.models import JixiaoTongji
import time

# Create your views here.
def index(request):
    logincode = request.GET['logincode']
    print('logincode='+logincode)

    userid = get_userid(get_access_token(), logincode)
    print('userid='+userid)
    return realindex(request, userid, True)
def logincheck(request):
    userid = request.COOKIES['user']
    print(userid)
    return realindex(request, userid, False)

def realindex(request, userid, firstlogin):
    try:
        user = User.objects.get(id = userid)
        mingci = JixiaoTongji.objects.get(user = user, year=time.localtime().tm_year, mon=time.localtime().tm_mon).mingci
        response = render_to_response('user/index.html', {'username':user.name, 'mingci':mingci})
        if firstlogin:
            response.set_cookie('user', str(user.id), max_age=60*60*2)
        return response
    except Exception as e:
        print(e.__class__)
        return HttpResponse('you are not belong yxdd')