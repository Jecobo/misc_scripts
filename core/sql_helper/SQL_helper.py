import time
import sqlite3
from lib import config
from rich.console import Console

console = Console()
#print(config.result_sql_path)


# url表  id url isAlive time url_tag
def url_table_create():
    conn = sqlite3.connect(config.result_sql_path)
    c = conn.cursor()
    try:
        c.execute(
            '''
                CREATE TABLE IF NOT EXISTS URLS(
                    ID INTEGER PRIMARY KEY,
                    URL TEXT NOT NULL,
                    isAlive TEXT DEFAULT "#",
                    status_code DEFAULT "#",
                    title DEFAULT "#",
                    URL_TIME TEXT NOT NULL,
                    URL_TAG TEXT NOT NULL
                );
            '''
        )
        conn.commit()
    except:
        console.print("[warning] URLS table exists...", style='bold yellow')
    console.print("[info] URLS table created...", style='bold blue')
    conn.close()


# url 插入数据库
def url_table_insert(urls, url_tag):
    url_conn = sqlite3.connect(config.result_sql_path)
    url_c = url_conn.cursor()
    for url in urls:
        url = url.strip()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            sql = '''
                INSERT INTO URLS (URL, URL_TIME, URL_TAG) VALUES ('%s', '%s', '%s')
            ''' % (url, now_time, url_tag)
            url_c.execute(sql)
            url_conn.commit()
        except:
            console.print("[error] url_table_insert() failed...", style='bold red')
    console.print("[info] url_table_insert() success...", style='bold blue')
    url_conn.close()


def url_table_read():
    url_conn = sqlite3.connect(config.result_sql_path)
    url_c = url_conn.cursor()
    try:
        urls = url_c.execute('select * from URLS').fetchall()
        console.print("[info] url_table_read() success...", style='bold blue')
        return urls
    except:
        console.print("[error] url_table_insert() failed...", style='bold red')
    url_conn.close()


def update_table_url(url, is_alive="#", status_code="#", title="#"):
    url_conn = sqlite3.connect(config.result_sql_path)
    url_c = url_conn.cursor()
    try:
        sql = "UPDATE URLS SET isAlive='%s',status_code='%s',title='%s' WHERE URL='%s'" % (is_alive, status_code, title, url)
        url_c.execute(sql)
        url_conn.commit()
    except:
        console.print("[error] update_table_url() failed...", style='bold red')
    console.print("[info] update_table_url() success...", style='bold blue')
    url_conn.close()


# 子域数据表检查
def subdomain_sql_check():
    conn = sqlite3.connect(config.result_sql_path)
    c = conn.cursor()
    # console.print('正在检查子域数据表是否存在，如不存在则自动新建', style="#ADFF2F")
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
        console.print("[warning] SUBDOMAIN exists...", style='bold yellow')
    finally:
        console.print("[info] SUBDOMAIN created...", style='bold blue')
        conn.close()


# 插入SUBDOMAIN数据库
def insert_subdomain_sql(subdomains, tag):     # tag 每次收集打个标签方便区分
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    # console.print('数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    for sub in subdomains:
        sub = sub.strip()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            subdomain_c.execute("INSERT INTO SUBDOMAIN (SUBDOMAIN, SUBDOMAIN_TIME, TAG) VALUES ('%s', '%s', '%s')" % (sub, now_time, tag))
            subdomain_conn.commit()
        except:
            console.print('[error] insert_subdomain_sql() failed...', style="bold red")

    console.print('[info] insert_subdomain_sql() success...',  style="bold blue")
    subdomain_conn.close()


# 读取SUBDOMAIN数据库
def read_subdomain_sql():
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    # console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        subdomains = subdomain_c.execute("select * from SUBDOMAIN").fetchall()
        console.print('[info] read_subdomain_sql() success...', style="bold blue")
        return subdomains
    except:
        console.print('[error] read_subdomain_sql() failed...', style="bold red")
    subdomain_conn.close()


def update_subdomain_sql(ip, cdn, domain):
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    # console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        sql = "UPDATE SUBDOMAIN set IP='%s',CDN='%s' WHERE SUBDOMAIN='%s'" % (ip, cdn, domain)
        subdomain_c.execute(sql)
        # subdomain_c.execute("UPDATE SUBDOMAIN set IP=?,CND=? WHERE ID=?", (ip, cdn, id))
        subdomain_conn.commit()
    except:
        console.print('[error] update_subdomain_sql() failed...', style="bold red")
    console.print('[info] update_subdomain_sql() success...', style="bold blue")
    subdomain_conn.close()


# 修改表结构
def add_table_column():
    add_conn = sqlite3.connect(config.result_sql_path)
    add_c = add_conn.cursor()
    try:
        sql = 'ALTER table URLS ADD title DEFAULT "#"'
        add_c.execute(sql)
        add_conn.commit()
    except Exception as e:
        print(e)
    finally:
        add_conn.close()

# add_table_column()
# subdomain_sql_check()


url_table_create()     # 调用就检查表是否创建
subdomain_sql_check()
# insert_subdomain_sql(domain_li, "test")
# print(read_subdomain_sql())
# update_subdomain_sql("11111", "s1111", '3')
# print(read_subdomain_sql())
