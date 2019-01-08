# -*- coding:utf-8 -*-
# author:MurphyWan

# 并不做什么事情，只是将flask的事件记录进来
from application import  app
from flask import request, redirect, g
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
import re


@app.before_request # 就是自动识别
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']

    #请求之前的一个方法; 在所有的请求在达到我们的controllers之前，我们都把它拦截下来

    # 编写逻辑是，如果用户请求一级等所有菜单都需要登录，那么就是拿cookie进行验证的; 引入request变量
    path = request.path

    # 判断是否为静态文件
    pattern = re.compile( '%s'% "|".join( ignore_check_login_urls ) ) # 将我们的配置文件做成了一个字符串
    if pattern.match( path ):
        return # 如果模式匹配了静态文件，就不需要做任何处理


    user_info = check_login()
    # g变量，默认等于空,这里需要from flask import g；如果这个人登录的话，我们就等于当前这个用户，然后在仪表盘(web/controller/index.py)页面就可以引入这个g变量
    g.current_user = None
    if user_info:
        g.current_user = user_info


    #判断是否正好为登录页面，如果正好是，则不作判断
    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match( path ):
        return


    #如果没有登录，就跳转到登录页面里面去。这里面用到两个库，一个是redirect;一个是UrlManager
    if not user_info:
        return redirect( UrlManager.buildUrl( "/user/login" ) )
    return



'''
check_login方法，判断用户是否已经登录
'''
# 如果没有登录，就要登录；如果已经登录了，我们就不用管TA了。
def check_login():
    # 第一步，取得cookie
    cookies = request.cookies
    auth_cookie = cookies[ app.config[ 'AUTH_COOKIE_NAME' ] ] if app.config[ 'AUTH_COOKIE_NAME' ] in cookies else None
    # app.logger.info( auth_cookie )

    '''
    cookie验证过程就是cookie对比过程，当时怎么加密，现在就怎么解密
    现在我们就知道当时在controllers/user/User.py中为什么会"%s#%s"中有“#”号，以及为什么我们会有一个生成授权码的方法geneAuthCode()了
    我们会从cookie中取出userID，然后从数据库中查出ta的个人信息，通过个人信息生成一个授权码，
    跟我们的cookie授权码进行对比，如果两个一致，那么匹配上了；如果不一致，那么cookie就是被别人修改的，就再次登录吧
    '''
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#") # 0是授权码，1是user ID
    if len( auth_info ) != 2:
        return False

    # 查用户信息
    try:
        # 如果能查到这条数据，说明这个人是存在的。
        user_info = User.query.filter_by( uid = auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode( user_info ):
        return False

    # 以上测试了所有的假，剩下的就是真，如下：
    return user_info

