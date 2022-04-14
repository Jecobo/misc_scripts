import time
import sqlite3
from lib import config
from rich.console import Console

console = Console()


# 子域数据表检查
def subdomain_sql_check():
    conn = sqlite3.connect("./test.db")
    c = conn.cursor()
    console.print('正在检查子域数据表是否存在，如不存在则自动新建', style="#ADFF2F")
    try:
        c.execute(
            '''CREATE TABLE IF NOT EXISTS SUBDOMAIN(
                    ID INTEGER PRIMARY KEY,
                    SUBDOMAIN TEXT NOT NULL,
                    IP TEXT DEFAULT "#",
                    CDN TEXT DEFAULT "#",
                    SUBDOMAIN_TIME TEXT NOT NULL,
                    TAG TEXT NOT NULL
                );
           '''
        )
        conn.commit()
    except:
        console.print('子域数据表已存在', style="bold red")


# 插入SUBDOMAIN数据库
def insert_subdomain_sql(subdomains, tag):     # tag 每次收集打个标签方便区分
    subdomain_conn = sqlite3.connect("./test.db")
    console.print('数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    for sub in subdomains:
        sub = sub.strip()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            subdomain_c.execute("INSERT INTO SUBDOMAIN (SUBDOMAIN, SUBDOMAIN_TIME, TAG) VALUES ('%s', '%s', '%s')" % (sub, now_time, tag))
            subdomain_conn.commit()
        except:
            console.print('插入子域数据库失败', style="bold red")
    console.print('插入子域数据库成功', style="#ADFF2F")
    subdomain_conn.close()


# 读取SUBDOMAIN数据库
def read_subdomain_sql():
    subdomain_conn = sqlite3.connect("./test.db")
    console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        subdomains = subdomain_c.execute("select * from SUBDOMAIN").fetchall()
        return subdomains
    except:
        console.print('读取子域数据库失败', style="bold red")
    console.print('读取子域数据库成功', style="#ADFF2F")
    subdomain_conn.close()


def update_subdomain_sql(ip, cdn, id):
    subdomain_conn = sqlite3.connect("./test.db")
    console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    print("xxxxxxx")
    try:
        sql = "UPDATE SUBDOMAIN set IP='%s',CDN='%s' WHERE ID='%s'" % (ip, cdn, id)
        subdomain_c.execute(sql)
        # subdomain_c.execute("UPDATE SUBDOMAIN set IP=?,CND=? WHERE ID=?", (ip, cdn, id))
        subdomain_conn.commit()
    except Exception as e:
        print(e)
        # .log("修改失败")
    console.log("修改成功")
    subdomain_conn.close()


# subdomain_sql_check()
# insert_subdomain_sql(['xxxxxx', 'dasdasdas'], "test")
# print(read_subdomain_sql())
# update_subdomain_sql("11111", "s1111", '3')
# print(read_subdomain_sql())
