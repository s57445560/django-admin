from django.db import models
GENDER_CHOICE = (
        (u'M', u'西山'),
        (u'F', u'北理工'),
    )
class UserInfo(models.Model):
    user = models.CharField(verbose_name="用户名", max_length=32)
    passwd = models.CharField(verbose_name="密码",max_length=32)
    role = models.ForeignKey('Direction',null=True,verbose_name="角色",on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="位置", max_length=4, choices=GENDER_CHOICE, default="F")
    tags = models.ManyToManyField('IP_host',verbose_name="主机")
    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = u'用户表'

class IP_host(models.Model):
    ip = models.CharField(max_length=32)

    def __str__(self):
        return self.ip
    class Meta:
        verbose_name_plural = u'ip地址表'

class Direction(models.Model):
    name = models.CharField(verbose_name='名称', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'方向（视频方向）'
