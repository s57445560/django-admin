from django.urls import resolve
from django.shortcuts import render,redirect,HttpResponse
from king_admin.permission_list import perm_dic
from django.conf import settings
from king_admin import models


def perm_check(*args,**kwargs):

    request = args[0]
    resolve_url_obj = resolve(request.path)
    current_url_name = resolve_url_obj.url_name  # 当前url的url_name
    #match_flag = False
    match_key = None
    permission_list = []
    user = "sunyang"
    match_results = [False]


    for permission_key,permission_val in perm_dic.items():

        per_url_name = permission_val[0]
        per_method  = permission_val[1]
        perm_args = permission_val[2]
        perm_kwargs = permission_val[3]

        if per_url_name == current_url_name: #matches current request url
            if per_method == request.method: #matches request method
                # if not  perm_args: #if no args defined in perm dic, then set this request to passed perm

                #逐个匹配参数，看每个参数时候都能对应的上。
                args_matched = False #for args only
                for item in perm_args:
                    request_method_func = getattr(request,per_method)
                    if request_method_func.get(item,None):# request字典中有此参数
                        args_matched = True
                    else:
                        print("arg not match......")
                        args_matched = False
                        break  # 有一个参数不能匹配成功，则判定为假，退出该循环。
                else:
                    args_matched = True
                #匹配有特定值的参数
                kwargs_matched = False
                for k,v in perm_kwargs.items():
                    request_method_func = getattr(request, per_method)
                    arg_val = request_method_func.get(k, None)  # request字典中有此参数
                    print("perm kwargs check:",arg_val,type(arg_val),v,type(v))
                    if arg_val == str(v): #匹配上了特定的参数 及对应的 参数值， 比如，需要request 对象里必须有一个叫 user_id=3的参数
                        kwargs_matched = True
                    else:
                        kwargs_matched = False
                        break # 有一个参数不能匹配成功，则判定为假，退出该循环。
                else:
                    kwargs_matched = True



                match_results = [args_matched,kwargs_matched]
                print("--->match_results ", match_results)
                if all(match_results): #都匹配上了
                    match_key = permission_key
                    break




    if all(match_results):
        b1 = models.UserInfo.objects.filter(user=user).last()
        if not b1:
            return False

        groups_objs = b1.to_group.all()
        control_objs = b1.to_control.all()
        for obj in groups_objs:
            to_control_objs = obj.to_control.all()
            for to_control in to_control_objs:
                permission_list.append(to_control.code)
        for obj in control_objs:
            permission_list.append(obj.code)

        if match_key in permission_list:
            print('当前用户有此权限')
            return True
        else:
            print('当前用户没有该权限')
            return False

    else:
        print("未匹配到权限项，当前用户无权限")





def check_permission(func):
    def inner(*args,**kwargs):
        if not perm_check(*args,**kwargs):
            request = args[0]
            return render(request,'king/403.html')
        return func(*args,**kwargs)
    return  inner
