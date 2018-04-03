#!/usr/bin/python
from king_admin import custom_perm_logic


perm_dic = {

    'king_admin_table_obj_get': ['table_obj', 'GET', [], {}, custom_perm_logic.only_view_own_customers],  # 可以查看CRM APP里所有数据库表
    'king_admin_table_obj_change_get': ['table_obj_change', 'GET', [], {},],  # 可以查看CRM APP里所有数据库表
    'king_admin_table_obj_change_post': ['table_obj_change', 'POST', [], {}, ],  # 可以查看CRM APP里所有数据库表
}
