# -*- coding: utf-8 -*-
# 2019/01/26 01 账号管理
from flask import Blueprint,request,redirect
from common.libs.Helper import ops_render, iPagination
from common.models.User import User
from common.libs.UrlManager import UrlManager
from application import app,db


route_account = Blueprint( 'account_page',__name__ )

@route_account.route( "/index" )
def index():
    # 账号列表展示，从数据库中读取出来，然后展示即可
    # 首先从common.models.User中导入User
    # 全量查询，分页功能一会儿再说;用uid这个字段进行倒序排列;.all()取出所有的数据，得到一个list
    # 将这个list传递到展示页面就可以展示了;定义一个resp_data
    resp_data ={} # 定义一个json变量
    req = request.values # 为了拿到当前页数

    page = int( req['page'] ) if ( 'page' in req and req['page'] ) else 1

    # 取总页数
    query = User.query
    # query.count()
    page_params = {
        'total': query.count(), # 要知道总共多少页
        'page_size': app.config['PAGE_SIZE'],
        'page': page,  # 当前页数
        'display':app.config['PAGE_DISPLAY'] ,
        'url':'/account/index',       # 希望我们每一页的url地址是多少; 这里可以写死，也可以用灵活的方式
    }

    pages = iPagination( page_params )
    offset = ( page - 1 ) * app.config['PAGE_SIZE']  # offset是偏移量; 这里因PAGE_SIZE是50，所以第一页从0开始，第二页从50开始
    limit = app.config['PAGE_SIZE'] * page # 每一页我们取多少



    list = query.order_by( User.uid.desc() ).all()[ offset:limit ] # limit进行分页计算
    resp_data['list'] = list
    resp_data['pages'] = pages

    return ops_render( "account/index.html", resp_data ) # 将list的值通过jason变量传进来；打开模板页面template/account/index.html
    # 接下来，我们开始讨论分页，要知道总共有多少条记录？每页显示多少条？一共几页？Flask有插件支持分页功能，不过这种比较简单的功能，建议不要使用插件了


# 详情 2019/02/02
# 通过当前的id取得是谁，然后进行展示就可以了
@route_account.route( "/info" )
def info():
    resp_data = {}
    req = request.args # request.args,与request.values的区别，args是只取get参数；values是是将我们所取的所有参数拼装好放入dict
    uid = int( req.get('id', 0 ) )
    reback_url = UrlManager.buildUrl("account/index")
    if uid < 1:        # 如果小于1说明没有
        return redirect( reback_url ) #那么就直接返回到页表页面


    info = User.query.filter_by( uid = uid ).first() # 先查一下这条uid是否存在
    if not info:       # 如果查不到这个人，就回到列表页面
        return redirect( reback_url )


    resp_data['info'] = info # 如果查到，就把信息传到前端展示就可以了

    return ops_render( "account/info.html", resp_data )

@route_account.route( "/set" )
def set():
    return ops_render( "account/set.html" )
