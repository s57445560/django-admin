#!/usr/bin/python
import re



def only_view_own_customers(request,*args,**kwargs):
    print('perm test',request,args,kwargs)
    print(request.path) 
    consultant = request.GET.get('user')
    #if consultant_id:
    #    consultant_id = int(consultant_id)
    #
    #print("consultant=1",type(consultant_id))
    p = re.compile(r"/userinfo")

    if not p.findall(request.path):
        return True
 
    if consultant == request.session.get('user',None):
        return True
    else:
        print("\033[31;1muser can only view his's own customer...\033[0m")
        return False
