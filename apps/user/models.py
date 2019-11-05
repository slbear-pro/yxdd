from django.db import models

# Create your models here.
class User(models.Model):
    BUMEN_CHOICE = (
        (0,'大队部'),
        (1,'驻外'),
    )
    id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="userid")
    name = models.CharField(max_length=20, verbose_name='姓名')
    bumen = models.SmallIntegerField(default=0, choices= BUMEN_CHOICE, verbose_name='部门')#用于点名时的显示
    jiaose = models.CharField(max_length=50,null=True,blank=True, verbose_name='角色')
    class Meta:
        db_table = 'yx_user'
        verbose_name = 'minjing'
        verbose_name_plural = verbose_name