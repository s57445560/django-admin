admin_web是什么？
====
<br>
<br>

这是一个django的`自定义插件`，他可以实现，对表的`增删改查`，`分页`，`搜索`，`自定制批量操作`，`权限配置`等。
<br>

配置说明
------- 
		templates/index_base.html 需要替换成自己的模板文件。
		
		king_admin/king_admin.py 用来配置对表的自定制项。
                
		修改 king_admin.py
		BaseAdmin 是父类，用来继承。
		register(models.UserInfo, UserInfoAdmin) 用来注册表的信息
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

		在项目内的urls.py中添加 king_admin url分支。
		url(r'king_admin/', include('king_admin.urls')),

		查询表信息的规则是:
		http://127.0.0.1:8000/king_admin/项目名/项目下的表


权限说明
-------
		king_admin/permission_list.py 写权限的格式
		perm_dic={
		 
		    'crm_table_index':['table_index','GET',[],{},custom_perm_logic.only_view_own_customers],  #可以查看CRM APP里所有数据库表
		    'crm_table_list':['table_list','GET',[],{}],    #可以查看每张表里所有的数据
		    'crm_table_list_view':['table_change','GET',[],{}],#可以访问表里每条数据的修改页
		    'crm_table_list_change':['table_change','POST',[],{}], #可以对表里的每条数据进行修改
		 
		    }
		　　
		
		字典里的key是权限名， 一会我们需要用过这些权限名来跟用户进行关联
		
		后面values列表里第一个值如'table_index'是django中的url name，在这里必须相对的url name,
		而不是绝对url路径，因为考虑到django url正则匹配的问题，搞绝对路径，不好控制。 
		values里第2个值是http请求方法
		values里第3个[]是要求这个请求中必须带有某些参数，但不限定对数的值是什么
		values里的第4个{}是要求这个请求中必须带有某些参数，并且限定所带的参数必须等于特定的值
		values里的第5个{}是钩子函数，可以写业务逻辑的权限控制，粒度更细。此此函数也可以不加

		king_admin 下有3张表
		Group    组表
		UserInfo 用户表
		Control  权限设置表    表内code字段对应permission_list.py内的 key字段

		通过对表内添加数据来控制用户权限
		permission.py 内的 user字段在应用场景的时候需要修改为session内获取
		custom_perm_logic.py 写业务逻辑的权限控制，返回要求为 True 或 False


		使用装饰器来对视图做权限认证

		from king_admin import permission
		@permission.check_permission		# 装饰器名称
