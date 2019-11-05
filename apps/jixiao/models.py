from django.db import models

# Create your models here.
class Cache(models.Model):
    key = models.CharField(max_length='20', primary_key=True)
    value = models.CharField(max_length='50', null=False)
    class Meta:
        db_table = 'yx_cache'

class WrongForm(models.Model):
    instanceid = models.CharField(max_length='50', null=False)
    class Meta:
        db_table = 'yx_wrongform'

class Jixiao(models.Model):
    process_instance_id = models.CharField(max_length='50', null=False,blank=True, verbose_name='process_instance_id')
    user = models.ForeignKey('user.User', verbose_name='姓名')
    time = models.DateField(verbose_name='加分日期')
    comment = models.CharField(max_length=200, verbose_name='加分项目')
    fenzhi = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='分值')
    result = models.CharField(max_length=20, null=True, blank=True, verbose_name='result')
    status = models.CharField(max_length=20, null=True, blank=True, verbose_name='status')
    class Meta:
        db_table = 'yx_jixiao'
        verbose_name = "绩效"
        verbose_name_plural = verbose_name

class JixiaoTongji(models.Model):
    user = models.ForeignKey('user.User', verbose_name='姓名')
    year = models.CharField(max_length=4, null=True, verbose_name='year')
    mon = models.CharField(max_length=2, null=True, verbose_name="月份")
    zongfen = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='总分')
    mingci = models.IntegerField(null= True, verbose_name='名次')
    class Meta:
        db_table = 'yx_jixiaoTongji'
        verbose_name = '绩效月报'
        verbose_name_plural = verbose_name

