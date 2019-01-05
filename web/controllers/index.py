# coding:utf-8
# author:MurphyWan

from flask import Blueprint,render_template

route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    return render_template( "index/index.html")
    # 上句因为有了在application.py的app = Application(__name__, template_folder=os.getcwd() + '/web/templates/', root_path = os.getcwd())的布局
    # 0003所以这里可以直接用
#一般是怎么加载我们的蓝图，一般是放在www.py中
