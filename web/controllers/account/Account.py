# -*- coding: utf-8 -*-
# 2019/01/26 01 账号管理
from flask import Blueprint
from common.libs.Helper import ops_render
from common.models.User import User


route_account = Blueprint( 'account_page',__name__ )

@route_account.route( "/index" )
def index():
    # 账号列表展示，从数据库中读取出来，然后展示即可
    # 首先从common.models.User中导入User
    # 全量查询，分页功能一会儿再说;用uid这个字段进行倒序排列;.all()取出所有的数据，得到一个list
    # 将这个list传递到展示页面就可以展示了;定义一个resp_data
    resp_data ={} # 定义一个json变量
    list = User.query.order_by( User.uid.desc() ).all()
    resp_data['list'] = list

    return ops_render( "account/index.html", resp_data ) # 将list的值通过jason变量传进来；打开模板页面template/account/index.html

@route_account.route( "/info" )
def info():
    return ops_render( "account/info.html" )

@route_account.route( "/set" )
def set():
    return ops_render( "account/set.html" )
