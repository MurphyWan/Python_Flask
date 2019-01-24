# -*- coding:utf-8 -*-
# author:MurphyWan

from flask import Blueprint  # 引入蓝图，因为要顶一个route_user
from flask import request  # 7-3 登录推出
from flask import jsonify, g
from common.models.User import User
from common.libs.user.UserService import UserService
from flask import make_response
import json
from application import app, db
from flask import redirect
from common.libs.UrlManager import UrlManager
from common.libs.Helper import ops_render

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
        return ops_render("user/login.html")  # 将练习文档中事先准备好的static和templates文件夹复制到web目录下
    # 问什么还是报错，说找不到模板？是因为application.py中重构了MVC架构，而默认的template目录是在app（应用程序根目录）中的
    # 所以，为了解决这个问题，我们要改写application.py中的内容def __init__(self, import_name， template_folder = ),增加若干参数

    # 2019年01月01日，首先获取登录功能的变量
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    # 登录参数的有效性判断

    if login_name is None or len(login_name) < 1:
        # 如果登录名为空，则返回登录失败，这里定义一个jason resp
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名！"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        # 如果登录名为空，则返回登录失败，这里定义一个jason resp
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录密码！"
        return jsonify(resp)

    # 校验用户名
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户登录名和密码！-1"
        return jsonify(resp)

    # 校验密码；密码和salt是通过某种算法的出来的，所以
    # 这里在 common/libs目录下创建user python包，并在其中创建UserService.py，即用户服务类

    # common/libs/user/建立完毕UserService这个类之后，我们就可以验证了
    if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户登录名和密码！-2"
        return jsonify(resp)

    # 一般都是用cookie的方式来存储，不用session，当session存在多台服务器上的情况，存在不共享的情况，需要用一种非常复杂的方式处理。
    # cookie的好处是，放在客户端。这里import make_response，制造一个返回头
    # response = make_response(json.dumps(resp))  # 需要返回的是登录成功
    response = make_response(json.dumps({ 'code':200, 'msg':'登录成功~~' }))  # 需要返回的是登录成功
    # 设置cookie;set_cookie (cookie名，cookie值)
    # response.set_cookie( "mooc_food", "%s#%s"%( "", user_info.uid) ) # 用"#"号拼接; cookie是明文的，所以要对前面%s要进行加密;
    # 打开UserService.py 实现上述的加密过程,定义静态方法geneAuthCode()
    # response.set_cookie("mooc_food", "%s#%s" % (
    # UserService.geneAuthCode(user_info), user_info.uid))  # 这里需要引入我们的配置，所以需要引入applicatoin中的app -->
    # -->在se_setting.py中增加 AUTH_COOKIE_NAME,值为"mooc_food"

    #将上文的"mooc_food"，通过配置文件方式改写，这样，以后该cookie就该配置更新就好，不要去提交代码了。新的方式如下：
    response.set_cookie( app.config['AUTH_COOKIE_NAME'], "%s#%s" % ( UserService.geneAuthCode(user_info), user_info.uid ) , 60*60*24*120)

    #然后,注释掉原有的return jsonify(resp)，将response返回就可以啦
    return response

    #return jsonify(resp)  # 测试下上面的两个变量个是否可用
    # 一般我们异步提交时才会这么使用的，所以代开login.html，将form 换成div,将action删掉；写一个ajax提交；本系统大部分使用异步提交，为了增强用户的使用方式


@route_user.route("/edit", methods = [ "GET", "POST" ] )
def edit():
    if request.method == "GET" :
        return ops_render("user/edit.html")

    resp = { 'code':200, 'msg':'操作成功～', 'data':{} }
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''

    if nickname is None or len( nickname ) < 1:
        resp['code']  = -1
        resp['msg'] = "请输入符合规范的姓名～"
        return jsonify( resp )

    if email is None or len( email ) < 1:
        resp['code']  = -1
        resp['msg'] = "请输入符合规范的邮箱～"
        return jsonify( resp )

    #当前用户已经查出来了，所以不用再查了。读出来就好。;引入g变量？？？
    user_info = g.current_user
    #将user的nickname和email进行更新
    user_info.nickname = nickname
    user_info.email = email

    #然后进行统一的数据库提交;import db
    db.session.add( user_info )
    db.session.commit()

    #统一提交完成后，我们就告诉用户更改成功了
    return jsonify(resp)





# 依然是用GET和POST两种方式展示提交的
@route_user.route("/reset-pwd", methods= ["GET","POST"])
def resetPwd():
    # 如果请求是GET，我们就进行展示就可以了
    if request.method == "GET":
        return ops_render("user/reset_pwd.html")

    resp = { 'code':200, 'msg':'操作成功', 'data':{} }
    req = request.values


    old_password = req['old_password'] if  'old_password' in req else ''
    new_password = req['new_password'] if  'new_password' in req else ''

    # 同样进行参数有效性判断,对原密码和新密码
    if old_password is None or len(old_password) <6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的原始密码"
        return jsonify(resp)
    #新密码要进行2次判断，空或者长度不足
    if new_password is None or len(new_password) <6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码"
        return jsonify(resp)
    #新旧密码一样
    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = "请重新输入符合规范的新密码，新旧密码不能相同哦！"
        return jsonify(resp)
    #以上参数已经校验完了。

    # 下一步,进行密码的更改。同样的从g.current_user取出当前的uesr对象
    user_info = g.current_user
    #注意，修改密码可不是明文哦！！！UserService.py
    user_info.login_pwd = UserService.genePwd( new_password , user_info.login_salt)

    db.session.add( user_info )
    db.session.commit() #统一提交数据库

    #统一进行一次cookie的刷新，类似于登录功能,将登录功能的代码复制过来就可以啦
    response = make_response(json.dumps( resp )) #改成resp统一回归
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s#%s" % (UserService.geneAuthCode(user_info), user_info.uid), 60*60*24*120) #保存120天


    return jsonify( resp ) #统一提交返回





# 退出 ; 这个功能比较简单，只需要将cookie清空完了就可以退出了。具体就是清理cookie，并且跳到登录页面。
@route_user.route( "/logout" )
def logout():
    response = make_response( redirect( UrlManager.buildUrl( "/user/login" ) ) )
    response.delete_cookie( app.config[ 'AUTH_COOKIE_NAME' ] ) # 清空cookie
    return response