# -*- coding: utf-8 -*-
import os, sys
import pymysql

def connect_mysql(hostname, username, passwd, database, db_port):
    try:
        conn = pymysql.connect(host=hostname,user=username,
        password=passwd,db=database,port=db_port, charset='utf8')
    except Exception as e:
        print(e)
        print(">> 连接数据库失败")
        sys.exit()
    print(">> 连接数据库成功")
    return conn;

def close_resouce(conn):
    conn.commit()
    conn.close()
    print(">> 连接资源已释放")

def insert_data(conn, sql, value):
    cursor=conn.cursor()
    try:
        cursor.executemany(sql,value)
    except Exception as e:
        print(e)
        print(">> 插入数据失败")
        sys.exit()
    print(">> 插入数据成功")
    cursor.close()

def select_data(conn, sql):
    cursor=conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(">> 查询数据失败")
        print(e)
        sys.exit()
    print(">> 查询数据成功")
    data=cursor.fetchall()
    cursor.close()
    return data;

if __name__=="__main__":
    hostname = "localhost"
    username = "root"
    passwd = "123456"
    database = "address"
    db_port = 3306
    conn = connect_mysql(hostname, username, passwd, database, db_port)

    insert_sql="insert into address(name, address) values(%s, %s)"
    insert_value=(("zhangsan","haidian"),("lisi","haidian"))
    insert_data(conn, insert_sql, insert_value)

    select_sql="select * from address"
    data = select_data(conn, select_sql)
    print(">> 查询数据如下")
    if data:
        for x in data:
            print(x)

    close_resouce(conn)
