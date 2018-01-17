from admin_a import models
from django.shortcuts import render,redirect
register_dic = {}

# 父类 初始化数据，字典格式的 key：表的字段名，value 填写字段的中文名称。
# list_display 设置前端现实的字段有哪些 必须填写id, 也可以填写自定义的字段,然后必须写一个函数
# list_filter 前端现实的搜索项目有哪些 select
# list_search 设置可以查找的字段
# page_number 设置一页有多少数据显示
# ordering 设置默认排序使用那个字段，如果不设置则使用id排序
# actions 设置动作，并且编写函数
# readonly_fields 设置只读字段
# readonly_table 设置整张表的只读
# filter_horizontal 复选框的格式
# one_field 表示只能唯一的字段
# note_field 显示鼠标悬停的效果，默认使用note的表字段来做效果，也可以自定义，这个为一个str

class BaseAdmin(object):
    list_display = []
    list_filter = []
    list_search = []
    page_number = 10
    readonly_fields = []
    ordering = None
    readonly_table = False
    note_field = 'note'
    actions = ['delect_select_objs',]
    filter_horizontal = []
    one_field =[]
    # 这个是默认自带的删除action功能
    def delect_select_objs(self,request,querysets):
        app_name = self.module._meta.app_label
        table_name = self.module._meta.model_name
        select_id = ','.join([str(i.id) for i in querysets])
        if self.readonly_table:
            error = {"error_info": "此表已为只读，不可删除，此操作非法."}
        else:
            error = {}
        if request.POST.get('delect_data') == "yes":
            if not self.readonly_table:
                querysets.delete()
                return redirect(request.path)
        return render(request, 'king/king_table_delete.html',{'objs': querysets,
                                                              'app_name': app_name,
                                                              'table_name': table_name,
                                                              'action':request._admin_action,
                                                              'select_id':select_id,
                                                              "admin_class":self,
                                                              "error":error})
    # 用来设置action 前台显示的中文名字是什么
    delect_select_objs.select_info_name = u"删除动作"

    def default_form_validation(self):
        # 用户可以自定义的 clean方法，相当于django form里的 clean方法
        pass


class UserInfoAdmin(BaseAdmin):
    list_display = ('id','user','passwd','gender','sunyang')
    list_filter = ('user','passwd','role','gender','tags')
    list_search = ('user', 'passwd', 'role__name','tags__ip')
    ordering = 'user'
    actions = ['delect_select_objs', 'test']
    # readonly_fields = ('user','passwd','tags')
    note_field = 'role'
    readonly_table = False
    one_field = ['passwd']
    filter_horizontal = ('tags')
    def test(self,request,querysets):
        print("---->")

    test.select_info_name = u'测试动作'


    # 设置用户自己自定义的form验证
    # add_error用来添加错误信息，第一个字段为表的字段名，第二个是错误信息
    # def default_form_validation(self):
    #     err_list = []
    #     user_data = self.cleaned_data.get('passwd','')
    #     # 将错误的信息 传递到err_list列表内 然后统一返回给 clean
    #     if len(user_data) < 15:
    #         self.add_error("passwd","不能小于15")

    # 设置 list_display 自定义的字段，在数据库里没有的字段在前台展示，比如跳转到另外一个页面的链接等...
    def sunyang(self):
        return self.instance.id

    # 来设置自定字段的中文名称
    sunyang.name = "自定义字段"
    # def clean_passwd(self):
    #     print(len(self.cleaned_data.get("passwd")),self.cleaned_data.get("passwd"))
    #     if len(self.cleaned_data.get("passwd")) < 10:
    #         self.add_error("passwd","不能小于10字节")


class DAdmin(BaseAdmin):
    list_display = ('id','name')

class IPAdmin(BaseAdmin):
    list_display = ('id','ip')
    list_filter = ('ip',)
# register_dic 数据格式如下：
# {
#   app_name:
#   {table_name:admin_class}
#   }
def register(model_class,admin_class=None):
    app_name = model_class._meta.app_label
    table_name = model_class._meta.model_name
    if app_name not in register_dic:
        register_dic[app_name] = {}
    if admin_class == None:
        admin_class = BaseAdmin
    admin_class.module = model_class
    register_dic[app_name][table_name] = admin_class




register(models.UserInfo, UserInfoAdmin)
register(models.Direction, DAdmin)
register(models.IP_host, IPAdmin)