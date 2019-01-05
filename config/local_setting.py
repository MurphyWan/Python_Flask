# coding:utf-8
# author:MurphyWan
import pymysql

DEBUG = True  # Flask测试环境下debug模式是要开启的
SQLALCHEMY_ECHO = True #将我们左右的设备语句打印出来
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:256Mcktgpy@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'utf-8' #所有编码设置成utf-8