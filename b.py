# -*- coding: utf-8 -*-

from test import readfile as rfile
from sys import argv
from db import connect_mysql, select_data, close_resouce

if __name__=="__main__":

    hostname = "localhost"
    username = "root"
    passwd = "123456"
    database = "app"
    db_port = 3306
    conn = connect_mysql(hostname, username, passwd, database, db_port)

    select_sql="select * from t_todolist"
    data = select_data(conn, select_sql)
    print(">> 查询数据如下")
    if data:
        for x in data:
            print(x)

    close_resouce(conn)
