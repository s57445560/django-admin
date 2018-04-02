from django.contrib import admin

# Register your models here.

from king_admin import models

class UserInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('to_group', 'to_control')


admin.site.register(models.UserInfo,UserInfoAdmin)
admin.site.register(models.Control)
admin.site.register(models.Group)
