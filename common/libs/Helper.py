# -*- coding:utf-8 -*-
# author:MurphyWan
from flask import g, render_template


'''
自定义分页类 iPagination
'''
def iPagination( params ):
    import math

    ret = {
        "is_prev":1, # 是否有上一页
        "is_next":1, # 是否有下一页
        "from" :0 , # 从第几页
        "end":0, # 到第几页
        "current":0, # 当前是多少
        "total_pages":0, # 总共有多少页
        "page_size" : 0, # 每一页的大小
        "total" : 0, # 总共的记录数
        "url":params['url'] # 它的url地址
    }

    total = int( params['total'] )
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    display = int( params['display'] )
    total_pages = int( math.ceil( total / page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2 ) ) # 半圆，取一半，比如一共10页，这里就是5

    if page - semi > 0 :
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end'] + 1 )
    return ret


'''
统一渲染方法
'''

# 定义ops_render方法，包括模板名称和上下文两个参数
def ops_render( template, context ={} ):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template( template, **context )