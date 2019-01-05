# coding:utf-8
# author:MurphyWan

# 这个文件本身在生产环境是不需要的，这里只是解决并说明本地静态文件无法加载的问题
from flask import Blueprint, send_from_directory

# 0001 send_from_directory
"""
send_from_directory主要用于下载文件：
下面是一个文件的下载实例
 
复制代码
# encoding=utf-8
from flask import Flask
from flask import g
from flask import send_from_directory
from flask import url_for
import os.path
 
app = Flask(__name__)
dirpath = os.path.join(app.root_path,'upload')
@app.route("/download/<path:filename>")
def downloader(filename):
    return send_from_directory(dirpath,filename,as_attachment=True)
"""

from application import app

route_static = Blueprint('static', __name__)


@route_static.route("/<path:filename>")
def index(filename):
    # app.logger.info(filename)

    return send_from_directory(app.root_path + "/web/static/", filename)
