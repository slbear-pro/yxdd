from utils.ddutils import get_access_token, get_jixiao_listids, get_process_instance
from apps.jixiao.models import Jixiao, Cache, WrongForm, JixiaoTongji
from apps.user.models import User
from django.db.models import Sum, Q
import time

def getdata():
    print('[start getdata]', time.asctime())
    access_token = get_access_token()
    starttime = int(float(time.mktime(time.strptime('2019-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')))*1000)
    try:
        starttime = Cache.objects.get(key='lasttimestamp').value
    except Exception as e:
        print(e)
    endtime = int(float(time.time())*1000)
    print('[starttime]==', time.asctime(time.localtime(int(starttime)/1000)))
    print('[endtime]==', time.asctime(time.localtime(int(endtime)/1000)))
    #get jixiao id list
    jixiao_listids = get_jixiao_listids(access_token, starttime, endtime)

    #get instance by list id
    instance_list = []
    for i in jixiao_listids:
        instance_list.append(get_process_instance(access_token, i))
    #change instance to jixiao model
    jixiao_list = get_jixiao_list(instance_list)
    for i in jixiao_list:
        i.save()
    print('[save instance end]')
    try:
        cache = Cache.objects.get(key = 'lasttimestamp')
        cache.value = endtime
        cache.save()
    except Exception as e:
        cache = Cache()
        cache.key = 'lasttimestamp'
        cache.value = endtime
        cache.save()
    #update running report
    running_jixiaolist = Jixiao.objects.filter(Q(status= 'RUNNING') | Q(status= 'NEW'))
    print(running_jixiaolist)
    for i in running_jixiaolist:
        print('[instanceid=]',i.process_instance_id)
        instancedict = get_process_instance(access_token, i.process_instance_id)
        if instancedict.get('status') != i.status:
            i.status = instancedict.get('status')
            i.result = instancedict.get('result')
            i.save()

    #update month reporter
    create_tongji_form(time.localtime().tm_year, time.localtime().tm_mon)
    print('[create tongji_form end]')
    if time.localtime().tm_mday < 11:
        month_form()

def month_form():#every month ,finally form
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon -1
    if month == 0:
        year = year -1
        month = 12
    create_tongji_form(year, month)

def create_tongji_form(year, month):#every tongji
    alluser = User.objects.all()
    for user in alluser:
        queryset = Jixiao.objects.filter(user=user, time__year = year, time__month = month, result = 'agree', status = 'COMPLETED').aggregate(Sum('fenzhi'))
        # print(queryset)
        tongjidata = JixiaoTongji.objects.filter(user = user, year = year, mon = month)
        if tongjidata.exists() == False:
            tongjidata = JixiaoTongji()
        else:
            tongjidata = tongjidata[0]
        tongjidata.user = user
        tongjidata.year = year
        tongjidata.mon = month
        tongjidata.zongfen = queryset.get('fenzhi__sum', 0)
        if tongjidata.zongfen is None:
            tongjidata.zongfen = 0
        tongjidata.save()
    queryset = JixiaoTongji.objects.filter(year = year, mon = month).order_by('zongfen')
    recordnum = len(queryset)
    for jixiaotongji in queryset:
        jixiaotongji.mingci = recordnum
        recordnum -= 1
        jixiaotongji.save()


def get_jixiao_list(instance_list):
    jixiao_list = []
    for i in instance_list:
        process_instance_id = i.get('process_instance_id')
        username1 = i.get('username1')
        username2 = i.get('username2')
        date = i.get('date')
        if date is None:
            date = i.get('create_time').split(' ')[0]
        usr1_fenzhi = i.get('usr1_fenzhi')
        usr2_fenzhi = i.get('usr2_fenzhi')
        comment = i.get('comment')
        result = i.get('result')
        status = i.get('status')

        jixiao = Jixiao()
        jixiao.process_instance_id = process_instance_id
        try:
            user1 = User.objects.get(name=username1)
            jixiao.user = user1
        except Exception as e:
            wf = WrongForm()
            wf.instanceid = process_instance_id
            wf.save()
            continue

        jixiao.time = date
        jixiao.comment = comment
        jixiao.fenzhi = usr1_fenzhi
        jixiao.status = status
        jixiao.result = result
        jixiao_list.append(jixiao)
        if username2 != 'null' and usr2_fenzhi != 'null':
            jixiao2 = Jixiao()
            jixiao2.process_instance_id = process_instance_id
            try:
                user2 = User.objects.get(name=username2)
                jixiao2.user = user2
            except Exception as e:
                wf = WrongForm()
                wf.instanceid = process_instance_id
                wf.save()
                continue
            jixiao2.time = date
            jixiao2.comment = comment
            jixiao2.fenzhi = usr2_fenzhi
            jixiao2.status = status
            jixiao2.result = result
            jixiao_list.append(jixiao2)
    return jixiao_list
