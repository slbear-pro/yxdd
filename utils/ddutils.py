import requests
import time
import json

CORP_ID = 'ding4193c637920e69c435c2f4657eb6378f'
APP_KEY = 'dingguinjsmkiga24iuy'
# APP_SECRET = 'sVrBLCzRJoozWmg3W7gyVThF9AupTbTT8-1JBM0i2HSSs2pHcjQniVs9gIbk2Q3C'
APP_SECRET = 'DA8Lcx_UHWkv5PFJcLslVmdQVTQcGbbsMS5O_-lezbM4BFgIt8RFJR-dxVyOXC6c'
DEPT_ID = '43273481'  # 郧西大队部门ID
JIXIAO_PROCESS_CODE = 'PROC-5E478140-CBA0-4598-8F03-767ECD540639'


def get_access_token():
    print('get_access_token')
    url = 'https://oapi.dingtalk.com/gettoken'
    params = {
        'appkey': APP_KEY,
        'appsecret': APP_SECRET,
    }
    r = requests.get(url, params=params, timeout=60)
    try:
        r = r.json()
        if r.get('errcode') == 0:
            access_token = r.get('access_token')
            print('[access_token]:' + access_token)
            return access_token
        else:
             print(r)
             raise Exception('get dd data error')
    except Exception as e:
        # raise e
        print("error Exception" + e.str())
        raise e 

# get_access_token()

# 企业内部免登授权码获取userid
# code为前端获取的免登授权码
def get_userid(access_token, code):
    print('get_userid')
    url = 'https://oapi.dingtalk.com/user/getuserinfo'
    params = {
        'access_token': access_token,
        'code': code
    }
    try:
        r = requests.get(url, params=params, timeout=60)
        try:
            r = r.json()
            print(r)
            if r.get('errcode') == 0:
                return r.get('userid')
            else:
                return 'error'
        except Exception as e:
            return "error Exception" + e.__str__()
    except Exception as e:
        raise e



def  get_jixiao_listids(access_token, starttime, endtime, cursor=0):
    print('[get_jixiao_listids]')
    url = 'https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=' + access_token
    headers = {'Content-Type' : r'application/json'}
    listids = []
    while not cursor is None:
        params = {
            'process_code': JIXIAO_PROCESS_CODE,
            'start_time': starttime,
            'end_time': endtime,
            'cursor': cursor
        }
        try:
            r = requests.post(url, data=json.dumps(params), headers=headers, timeout=60)
            try:
                r = r.json()
                # print('r.json====success')
                if 'errcode' in r and r.get('errcode') == 0:
                    listids += r.get('result').get('list')
                    # print(listids)
                    cursor=r.get('result').get('next_cursor')
                else:
                    print('[errormsg]:', r.get('errcode'),r.get('errmsg'))
                    raise Exception('get dd data exception')
            except Exception as e:
                raise e
        except Exception as e:
            raise e
    print('[getjixiaolistids]循环完成:')
    print(listids)
    return listids


# starttime = int(time.mktime(time.strptime('2019-10-21-00-00-00', '%Y-%m-%d-%H-%M-%S')))*1000
# endtime = int(time.mktime(time.strptime('2019-10-21-23-00-00', '%Y-%m-%d-%H-%M-%S')))*1000
# get_jixiao_listids('1fd6af5172f13637884b8b901bba0f93', starttime, endtime)


def get_process_instance(access_token, process_instance_id):
    print("*"*20 + process_instance_id + '*'*20)
    url = 'https://oapi.dingtalk.com/topapi/processinstance/get?access_token='+access_token
    headers = {'Content-Type' : r'application/json'}
    params ={'process_instance_id': process_instance_id}
    try:
        r = requests.post(url, data=json.dumps(params), headers=headers, timeout=60)
        try:
            r = r.json()
            if r.get('errcode') == 0:
                form_list = r['process_instance']['form_component_values']
                # print('[form_list]:', form_list)
                instance_dict = {'process_instance_id':process_instance_id}
                for i in form_list:
                    if i.get('name') == '民警1':
                        instance_dict['username1'] = i['value']
                    elif i.get('name') == '民警2':
                        instance_dict['username2'] = i['value']
                    elif i.get('name') == '日期':
                        instance_dict['date'] = i['value']
                    elif i.get('name') == '具体事项':
                        instance_dict['comment'] = i['value']
                    elif i.get('name') == '民警1分值':
                        instance_dict['usr1_fenzhi'] = i['value']
                    elif i.get('name') == '民警2分值':
                        instance_dict['usr2_fenzhi'] = i['value']
                    else:
                        pass
                instance_dict['create_time'] = r['process_instance']['create_time']
                instance_dict['result'] = r['process_instance']['result']
                instance_dict['status'] = r['process_instance']['status']
                '''
                username1 = form_list[0]['value']
                # print('[username1]:', username1)
                username2 = form_list[1]['value']
                # print('[username2]:', username2)
                date = form_list[2]['value']

                comment = form_list[4]['value']
                # print('[content]:', comment)
                usr1_fenzhi = form_list[5]['value']
                # print('[usr1_fenzhi]', usr1_fenzhi)
                usr2_fenzhi = form_list[6]['value']
                # print('[usr2_fenzhi]', usr2_fenzhi)

                create_time = r['process_instance']['create_time']
                # print('[create_time]:', create_time)
                finish_time = r['process_instance'].get('finish_time')
                # print('[finish_time]:', finish_time)
                result = r['process_instance']['result']
                # print('[result]:'+ result)
                status = r['process_instance']['status']
                # print('[status]:'+ status)
                instance_dict = {'process_instance_id':process_instance_id,'username1':username1, 'username2':username2, 'date':date, 'usr1_fenzhi':usr1_fenzhi, 'usr2_fenzhi':usr2_fenzhi, 'comment':comment, 'create_time':create_time, 'result':result, 'status':status}
                '''
                print(instance_dict)
                return instance_dict
            else:
                print(r'[errcode]==[getinstance]')
                print(r)
                raise Exception('get dingding data error')
        except Exception as e:
            raise e   #r.json()出错
    except Exception as e:
        raise e #requests出错


# get_process_instance('2bec432cd32239aebaae48faa7c406b9', 'ff441692-0cab-4f3c-a608-66ced7606b51')



# starttime = int(time.mktime(time.strptime('2019-10-21-00-00-00', '%Y-%m-%d-%H-%M-%S')))*1000
# endtime = int(time.mktime(time.strptime('2019-10-21-23-00-00', '%Y-%m-%d-%H-%M-%S')))*1000
def ceshi():
    access_token = get_access_token()
    starttime = int(time.mktime(time.strptime('2019-11-01-00-00-00', '%Y-%m-%d-%H-%M-%S'))*1000)
    endtime = int(time.mktime(time.strptime('2019-11-02-23-00-00', '%Y-%m-%d-%H-%M-%S'))*1000)
    listids = get_jixiao_listids(access_token,starttime, endtime)
    for i in listids:
        get_process_instance(access_token, i)
    # print(starttime, endtime)



