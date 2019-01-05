# -*- coding:utf-8 -*-
# author:MurphyWan
import hashlib, base64


class UserService():
    '''
    写一些用户的核心操作和统一的方法都可以写在这个地方
    '''

    @staticmethod
    def genePwd(pwd, salt):
        '''
        产生密码
        根据用户的输入和加密字符串，来生成我们的参数
        非常简单，就是根据MD5、base64来生成；导入hashlib,base64
        :return:
        '''
        # 定义一个变量，初始化md5字符串
        m = hashlib.md5()
        # 将密码和盐拼接成一个字符串
        str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")),
                         salt)  # 这里通过base64的encodebytes给密码加密;另外，根据encodebytest方法说明，需要把密码转化成python的字节码，这里用到了str.encode("utf-8")
        # 用update方法
        m.update(str.encode("utf-8"))
        return m.hexdigest()  # 返回16进制的编码
