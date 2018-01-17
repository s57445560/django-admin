from django.contrib import admin

# Register your models here.
from admin_a import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'passwd',)
    list_filter = ('user',)
    search_fields = ('user',)
    list_editable = ('passwd',)


admin.site.register(models.UserInfo,ArticleAdmin)

class DAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Direction,DAdmin)

