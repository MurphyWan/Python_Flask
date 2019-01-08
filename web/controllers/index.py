# coding:utf-8
# author:MurphyWan
# 这也是仪表盘页面

from flask import Blueprint,render_template,g

route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    '''
    把当前用户的登录状态获取过来。在interceptors/AuthInterceptor.py中通过Flask的g变量获取
    引入g变量
    :return:
    '''
    current_user = g.current_user
    return render_template( "index/index.html", current_user = current_user) # 补充了current_user，就是在layout_main.html引入
    # 上句因为有了在application.py的app = Application(__name__, template_folder=os.getcwd() + '/web/templates/', root_path = os.getcwd())的布局
    # 0003所以这里可以直接用
#一般是怎么加载我们的蓝图，一般是放在www.py中


