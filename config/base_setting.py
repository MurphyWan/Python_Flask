# coding:utf-8
# author:MurphyWan
SERVER_PORT = 8999  # 然后在manager.py中端口处，以app.config['SERVER_PORT']获取配件文件的方式编写它
DEBUG = False  # Flask默认debug模式是不开启的
SQLALCHEMY_ECHO = False
# SQLALCHEMY_DATABASE_URI = 'mysql://root:256Mcktgpy@127.0.0.1/mysql'
# SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
1\增加以上两个变量，运行中的warning提示将会消失
2\manager.py作为本程序的入口，做好能有个扩展，这里引入一个非常好的工具,flask-script,相当于可以new一个manager
安装好这个扩展后，我们在application.py中引入这个包
"""
