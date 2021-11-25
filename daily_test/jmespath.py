#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 11:34 上午
# @Author  : xin
# @Detail  : jmespath解析json格式

from jmespath import search

data = [
    {"id": "321776", "created_at": 1632445303000, "updated_at": 1632445303000, "create_user_id": None,
     "update_user_id": None, "name": "新增类别+1632445274.4183846", "stock_part_id": None, "parent_id": None,
     "store_id": "1", "master_id": None, "share_category_id": None, "category_id": None,
     "parts_category_source": "本店", "source": 0, "parts_category_no": "77", "is_show_edit_and_delete_key": True,
     "is_delete": 0, "sub_store_ids": None, "sub_parts_category_list": None, "category_id_str": None,
     "child_category_type": None, "category_code": ""},
    {"id": "321777", "created_at": 1632446120000,
     "updated_at": 1632446120000, "create_user_id": None,
     "update_user_id": None, "name": "新增类别+1632446091.9929805",
     "stock_part_id": None, "parent_id": None, "store_id": "1",
     "master_id": None, "share_category_id": None,
     "category_id": None, "parts_category_source": "本店",
     "source": 0, "parts_category_no": "78",
     "is_show_edit_and_delete_key": True, "is_delete": 0,
     "sub_store_ids": None, "sub_parts_category_list": None,
     "category_id_str": None, "child_category_type": None,
     "category_code": ""},
    {"id": "1", "created_at": 1571744833000, "updated_at": 1632450923000, "create_user_id": None,
     "update_user_id": None, "name": "编辑类别+1632450894.0462174", "stock_part_id": None, "parent_id": None,
     "store_id": "1", "master_id": None, "share_category_id": None, "category_id": None, "parts_category_source": "本店",
     "source": 0, "parts_category_no": "1", "is_show_edit_and_delete_key": True, "is_delete": 0, "sub_store_ids": None,
     "sub_parts_category_list": None, "category_id_str": None, "child_category_type": None, "category_code": None}
]
exp = 'id'
get_data = search('id', data)

print(get_data)
