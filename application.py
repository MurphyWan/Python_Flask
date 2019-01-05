# coding:utf-8
# author:MurphyWan
# application.py 是封装Flask的全局变量，包括app，数据库等 (12/3)

from flask import Flask
# 承接base_setting.py第九行，引入flask-script这个，导入manager这个类
from flask_script import Manager
# 然后我们将app进行包装

from flask_sqlalchemy import SQLAlchemy
import os


# 定义一个类，Application，继承Flask
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path = None): # 0001<<
        # 然后修改app = Application(__name__, template_folder = os.getcwd()+"/web/templates/")
        super(Application, self).__init__(import_name, template_folder=template_folder,root_path = root_path, static_folder = None)
        # 0002 因为flask本来有默认的static目录，所以当我们用自己的MVC框架进行重构时，一定要把static_folder变量设置为None
        # template_folder模板文件，root_path存放模板的根目录。这里改的原因是我们定义MVC的结构和Flask默认的不同，所以要改
        # 从pyfile的base_setting.py加载配置
        self.config.from_pyfile('config/base_setting.py')  # --> 需要有一种方式加载local_setting.py,先复制一行
        # 定义一个环境变量, ops_config,可以选择运行环境
        if "ops_config" in os.environ:  # 引入os包
            # self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])
            self.config.from_pyfile('config\\%s_setting.py' % os.environ['ops_config'])  # windows中用两个反斜杠
            # 运行的时候，需要在命令行输入export ops_config=local or windows下用set ops_config=local，然后再运行python manager.py runserver
            # 这时候就是读取local_setting.py中的配置

        # 初始化变量
        db.init_app(self)


# app = Flask( __name__)
# 上面已经定义了一个Flask的子类Application，就是为了加载配置文件，所以这里就new一个Application
db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + '/web/templates/', root_path = os.getcwd())
# 因为上面类方法 __init__(self, import_name)中先初始化了db.init_app()方法，所以下面这句的位置，要放在app = Application(__name__)上面
# db = SQLAlchemy( app)


manager = Manager(app)
# 然后,在manager.py中引入manager,可以参考from application import app,manager

"""
函数模板
"""
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl,
                        'buildStaticUrl')  # 后面buildStaticUrl是方法名，将这UrlManager.buildStaticUrl类中的这个方法注入进来
app.add_template_global(UrlManager.buildUrl,
                        'buildUrl')  # 后面buildStaticUrl是方法名，将这UrlManager.buildStaticUrl类中的这个方法注入进来
# 将这两个方法注入到模板里面去
