from django.db import models

# Create your models here.
class Banci(models.Model):
    name = models.CharField(max_length=20, verbose_name='班次名称')
    index = models.IntegerField(verbose_name="index") #显示的前后顺序
    class Meta:
        db_table = 'yx_banci'
        verbose_name = '班次'
        verbose_name_plural = verbose_name

class PaiBan(models.Model):
    date = models.DateField(verbose_name="日期")
    banci = models.ForeignKey('Banci', verbose_name='班次')
    #添加两个外键导致反响查询冲突
    #userFirst = models.ForeignKey('user.User', verbose_name='民警1')
    #userSecond = models.ForeignKey('user.User', verbose_name='民警2', null=True, blank=True)
    userFirst = models.CharField(max_length=20, verbose_name='民警1')
    userSecond = models.CharField(max_length=20, verbose_name='民警2', null=True, blank=True)
    class Meta:
        db_table = 'yx_paiban'
        verbose_name = '排班表'
        verbose_name_plural = verbose_name