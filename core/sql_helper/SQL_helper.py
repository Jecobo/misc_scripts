import time
import sqlite3
from lib import config
from rich.console import Console

console = Console()
conn = sqlite3.connect(config.result_sql_path)


# 子域数据表检查
def subdomain_sql_check():
    c = conn.cursor()
    console.print('正在检查子域数据表是否存在，如不存在则自动新建', style="#ADFF2F")
    try:
        c.execute(
            '''CREATE TABLE SUBDOMAIN(
                    ID INTEGER PRIMARY KEY,
                    SUBDOMAIN TEXT NOT NULL,
                    SUBDOMAIN_TIME TEXT
                );
           '''
        )
        conn.commit()
    except:
        console.print('子域数据表已存在', style="bold red")


# 插入SUBDOMAIN数据库
def insert_subdomain_sql(subdomains):
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    console.print('数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    for sub in subdomains:
        sub = sub.strip()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            subdomain_c.execute("INSERT INTO SUBDOMAIN (SUBDOMAIN,SUBDOMAIN_TIME) VALUES ('%s', '%s')" % (sub, now_time))
            subdomain_conn.commit()
        except:
            console.print('插入子域数据库失败', style="bold red")
    console.print('插入子域数据库成功', style="#ADFF2F")
    subdomain_conn.close()


# 读取SUBDOMAIN数据库
def read_subdomain_sql():
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        subdomains = subdomain_c.execute("select * from SUBDOMAIN").fetchall()
        return subdomains
    except:
        console.print('读取子域数据库失败', style="bold red")
    console.print('读取子域数据库成功', style="#ADFF2F")
    subdomain_conn.close()
