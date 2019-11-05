from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


class my_mid:
    #def __init__(self):
       # pass
    def process_request(self, request):
        if(request.path.startswith('/admin/')):
            return

        if 'user' not in request.COOKIES:
            logincode = request.GET.get('logincode', None)
            print(logincode)
            if logincode is None:
                print('diyici')
                return render(request, 'user/login.html')
            else:
                print('dierci')
