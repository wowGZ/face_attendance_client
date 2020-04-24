"""
@version: 1.0
@author: WowGz
@blog: https://wowgz.com.cn
@file: DatabaseUtils
@time: 2020/4/24/024 21:38
"""
import pymysql


class DatabaseUtils:
    schema = 'attendance_system_springboot'
    password = '123456'
    user = 'root'
    url = 'localhost'

    @classmethod
    def insert_delete_update(cls, sql):
        connection = pymysql.connect(cls.url, cls.user, cls.password, cls.schema)
        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            connection.commit()
            print('---------------------------------------------------------------------------')
            print(sql + "execute success")
            print('---------------------------------------------------------------------------')
        except Exception as ex:
            print('---------------------------------------------------------------------------')
            print(f'execute failed.Case:{ex}' + sql)
            print('---------------------------------------------------------------------------')
        finally:
            connection.close()
