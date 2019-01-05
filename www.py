# coding:utf-8
# author:MurphyWan
# 蓝图放在www.py中

""" controller.py/index.py
from flask import Blueprint
route_index = Blueprint('index_page', __name__)
@route_index.route("/")
def index():
    return "Hello World"
"""
from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.account.Account import route_account  # 账号管理
from web.controllers.food.Food import route_food  # 商品管理
from web.controllers.member.Member import route_member  # 会员管理
from web.controllers.finance.Finance import route_finance  # 财务管理
from web.controllers.stat.Stat import route_stat  # 统计管理

# 注册蓝图
app.register_blueprint(route_index, url_prefix='/')
# 然后在入口文件manager.py中引入www.py，就是调用www中的所有变量

app.register_blueprint(route_user, url_prefix='/user')
app.register_blueprint(route_static, url_prefix='/static')
app.register_blueprint(route_account, url_prefix='/account')
app.register_blueprint(route_food, url_prefix='/food')
app.register_blueprint(route_member, url_prefix='/member')
app.register_blueprint(route_finance, url_prefix='/finance')
app.register_blueprint(route_stat, url_prefix='/stat')
