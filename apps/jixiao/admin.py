from django.contrib import admin
from apps.jixiao.models import Jixiao, JixiaoTongji
# Register your models here.
class JixiaoAdmin(admin.ModelAdmin):
    list_display = ['user', 'time', 'comment', 'fenzhi', 'status', 'result']

class JixiaoTongjiAdmin(admin.ModelAdmin):
    list_display = ['user', 'year', 'mon', 'zongfen', 'mingci']
admin.site.register(Jixiao, JixiaoAdmin)
admin.site.register(JixiaoTongji, JixiaoTongjiAdmin)