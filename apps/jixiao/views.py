from django.http import HttpResponse
from django.shortcuts import render
from utils.ddutils import get_access_token, get_jixiao_listids, get_process_instance
from apps.jixiao.models import Jixiao, Cache, WrongForm, JixiaoTongji
from apps.user.models import User
from django.db.models import Sum
from apps.jixiao.tasks import getdata
import time

# Create your views here.
def index(request):
    print('jixiao.index')
    userid = request.COOKIES['user']
    username = User.objects.get(id=userid).name
    year = time.localtime().tm_year
    mon = time.localtime().tm_mon
    jixiaotongji = JixiaoTongji.objects.filter(year=year, mon=mon).order_by('mingci')
    updatetime = ''
    try:
        updatetimestamp = Cache.objects.get(key='lasttimestamp').value
        updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(updatetimestamp)/1000))
    except Exception as e:
        print(e)
    return render(request, 'jixiao/index.html', {'username': username, 'jixiaotongji':jixiaotongji, 'updatetime': updatetime, 'year':year, 'mon':mon})

def mingxi(request, userid, year, mon):
    user = User.objects.get(id=userid)
    jixiaolist = Jixiao.objects.filter(time__year=year, time__month=mon, user=user, result='agree', status='COMPLETED')
    return render(request, 'jixiao/mingxi.html',{'Jixiaolist': jixiaolist})

def ceshi1(request):
    access_token = get_access_token()
    starttime = Cache.objects.get(key='lasttimestamp')
    endtime = int(float(time.time())*1000)
    jixiao_listids = get_jixiao_listids(access_token, starttime, endtime)

    instance_list = []
    jixiao_list = []
    for i in jixiao_listids:
        instance_list.append(get_process_instance(access_token, i))


    for i in instance_list:
        process_instance_id = i.get('process_instance_id')
        username1 = i.get('username1')
        username2 = i.get('username2')
        usr1_fenzhi = i.get('usr1_fenzhi')
        usr2_fenzhi = i.get('usr2_fenzhi')
        comment = i.get('comment')
        create_time = i.get('create_time')
        result = i.get('result')
        status = i.get('status')

        jixiao = Jixiao()
        jixiao.process_instance_id = process_instance_id
        try:
            user1 = User.objects.get(name = username1)
            jixiao.user = user1
        except Exception as e:
            wf = WrongForm()
            wf.instanceid = process_instance_id
            wf.save()
            continue
        jixiao.time = create_time.split(' ')[0]
        jixiao.comment = comment
        jixiao.fenzhi = usr1_fenzhi
        jixiao.status = status
        jixiao.result = result
        jixiao_list.append(jixiao)
        if username2 != 'null' and usr2_fenzhi != 'null':
            jixiao2 = Jixiao()
            try:
                user2 = User.objects.get(name=username2)
                jixiao2.user = user2
            except Exception as e:
                wf = WrongForm()
                wf.instanceid = process_instance_id
                wf.save()
                continue
            jixiao2.time = create_time.split(' ')[0]
            jixiao2.comment = comment
            jixiao2.fenzhi = usr2_fenzhi
            jixiao2.status = status
            jixiao2.result = result
            jixiao_list.append(jixiao2)

    for i in jixiao_list:
        i.save()

    cache = Cache.objects.get(key = 'lasttimestamp')
    cache.value = endtime
    cache.save()

def ceshi(request):
    getdata()
    # alluser = User.objects.all()
    # for user in alluser:
    #     queryset = Jixiao.objects.filter(user = user).aggregate(Sum('fenzhi'))
    #     print(user.id, user.name, queryset.get('fenzhi__sum', 0))
    # 102469322123349914 my id
    # user = User.objects.get(id = '102469322123349914')
    # queryset = Jixiao.objects.filter(user = user, time__year = 2019, time__month = 10, result = 'agree', status = 'COMPLETED')
    # for i in queryset:
    #     print(i.user.name)
    #     print(i.comment)
