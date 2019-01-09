# -*- coding:utf-8 -*-
# author:MurphyWan
from flask import g,render_template


'''
统一渲染方法
'''

# 定义ops_render方法，包括模板名称和上下文两个参数
def ops_render( template, context ={} ):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template( template, **context )