admin_web是什么？
====
<br>
<br>

这是一个django的`自定义插件`，他可以实现，对表的`增删改查`，`分页`，`搜索`，`自定制批量操作`等。
<br>

配置说明
------- 
		`templates/index_base.html` 需要替换成自己的模板文件。<br>
		
		`king_admin\king_admin.py` 用来配置对表的自定制项。<br>
		
		BaseAdmin 是父类，用来继承。<br>
		register(models.UserInfo, UserInfoAdmin) 用来注册表的信息<br>
		# 父类 初始化数据，字典格式的 key：表的字段名，value 填写字段的中文名称。<br>
		# list_display 设置前端现实的字段有哪些 必须填写id, 也可以填写自定义的字段,然后必须写一个函数<br>
		# list_filter 前端现实的搜索项目有哪些 select<br>
		# list_search 设置可以查找的字段<br>
		# page_number 设置一页有多少数据显示<br>
		# ordering 设置默认排序使用那个字段，如果不设置则使用id排序<br>
		# actions 设置动作，并且编写函数<br>
		# readonly_fields 设置只读字段<br>
		# readonly_table 设置整张表的只读<br>
		# filter_horizontal 复选框的格式<br>
		# one_field 表示只能唯一的字段<br>
		# note_field 显示鼠标悬停的效果，默认使用note的表字段来做效果，也可以自定义，这个为一个str<br>
