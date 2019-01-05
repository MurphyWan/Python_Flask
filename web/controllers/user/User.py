# coding:utf-8
# author:MurphyWan

from flask import Blueprint  # 引入蓝图，因为要顶一个route_user
from flask import render_template
from flask import request # 7-3 登录推出
from flask import jsonify

# 以下是后台仪表盘前端页面的三个页面 ，登录、编辑和修改密码页面
route_user = Blueprint('user_page', __name__)


@route_user.route('/login', methods=["GET", "POST"])
def login():
    # 用个判断来进行登录验证，GET用于显示页面，POST用于登录
    if request.method == "GET":
    # return "login"
    # run ， 打开浏览器，输入127.0.0.1:8999/user/login，发现404。是因为我们用www.py统一root加载一行
    # from web.controllers.user.User import route_user
    # 渲染页面
        return render_template("user/login.html")  # 将练习文档中事先准备好的static和templates文件夹复制到web目录下
    # 问什么还是报错，说找不到模板？是因为application.py中重构了MVC架构，而默认的template目录是在app（应用程序根目录）中的
    # 所以，为了解决这个问题，我们要改写application.py中的内容def __init__(self, import_name， template_folder = ),增加若干参数

    # 2019年01月01日，首先获取登录功能的变量
    resp = { 'code':200, 'msg':'登录成功', 'data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    #登录参数的有效性判断

    if login_name is None or len( login_name ) < 1:
        #如果登录名为空，则返回登录失败，这里定义一个jason resp
        resp[ 'code' ] = -1
        resp[ 'msg' ] = "请输入正确的登录用户名！"
        return jsonify( resp )

    if login_pwd is None or len( login_pwd ) < 1:
        #如果登录名为空，则返回登录失败，这里定义一个jason resp
        resp[ 'code' ] = -1
        resp[ 'msg' ] = "请输入正确的登录密码！"
        return jsonify( resp )


    return "%s - %s"%( login_name, login_pwd) # 测试下上面的两个变脸个是否可用




@route_user.route("/edit")
def edit():
    return render_template( "user/edit.html")

@route_user.route( "/reset-pwd")
def resetPwd():
    return render_template("user/reset_pwd.html")