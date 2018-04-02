from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=32,verbose_name="组名")
    to_control = models.ManyToManyField('Control',verbose_name="权限选择",blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'权限组表'


class Control(models.Model):
    code = models.CharField(max_length=32,verbose_name="权限对应代码")
    name = models.CharField(max_length=32,verbose_name="权限名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'权限表'


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    name = models.CharField(max_length=32,verbose_name="用户姓名")
    to_group = models.ManyToManyField('Group',verbose_name="组的选择",blank=True)
    to_control = models.ManyToManyField('Control',verbose_name="权限的选择",blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'用户权限'

