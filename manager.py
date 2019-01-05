# coding:utf-8
# author:MurphyWan
# manager.py 引入变量， 如app (12/3)
# 开头第一句就是 from applicatioin import app,引入app这个变量
from application import app, manager  # 用来支持app.run(host='0.0.0.0', debug=True)这样的写法
from flask_script import Server
import www

# 好处是可以自定义命令，如下：
## web server                                    下方是因为在base_setting设置端口好了，这里调用即可
manager.add_command("runserver", Server(host='0.0.0.0', port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))
# 以上，以后有了job方式后，可以用runjob的方式运行程序
# 接着，我们实现了base_setting.py配置，我们还有develop_setting/ local_seeting.py/ production_setting.py，需要实现--> applicaiton.py

# 以上 在引入manager之后，可以引入flask_script很多特性，比如server
from flask_script import Server


def main():  # main方法是什么都不干，就是定义一个run方法 ; 在引入flask_script之后，有了manager和Sever,这里可以把原本的app.run(host='0.0.0.0', debug=True)，改成以下内容
    manager.run()
    # 在运行一下，提示无法跑了，提示如下：
    # 可以通过python manager.py runserver来运行
    # 然后在base_setting.py中配置一下端口
    """
    D:\Work\Python\wxminiapp\miniaec_self>python manager.py
usage: manager.py [-?] {runserver,shell} ...

positional arguments:
  {runserver,shell}
    runserver        Runs the Flask development server i.e. app.run()
    shell            Runs a Python shell inside Flask application context.

optional arguments:
  -?, --help         show this help message and exit

    """


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
        """
        exit([status])

        Exit the interpreter by raising SystemExit(status).
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
        """
    except Exception as e:
        import traceback  # python中引入traceback包，可以把所有的错误打印出来

        traceback.print_exc()
# 以上就是我们所有的环境

# run 之后会出现以下信息，说明缺少SQLalchemy配置，SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS，SQLALCHEMY_TRACK_MODIFICATIONS
# 因为我们的用了Flask高可用MVC框架，所以，这里SQLalchemy的配置在base_setting.py中进行
"""
D:\Work\Python\wxminiapp\miniaec_self>python manager.py
C:\Python35\lib\site-packages\flask_sqlalchemy\__init__.py:774: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_UR
I to "sqlite:///:memory:".
  'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
C:\Python35\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by def
ault in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "application" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Python35\lib\site-packages\flask_sqlalchemy\__init__.py:774: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_UR
I to "sqlite:///:memory:".
  'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
C:\Python35\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by def
ault in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Debugger is active!
 * Debugger PIN: 294-404-712
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Dec/2018 15:02:49] "GET / HTTP/1.1" 404 -

"""
