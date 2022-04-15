import time
import sqlite3
from lib import config
from rich.console import Console

console = Console()


# url表  id url isAlive time url_tag
def url_table_create():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    try:
        c.execute(
            '''
                CREATE TABLE IF NOT EXISTS URLS(
                    ID INTEGER PRIMARY KEY,
                    URL TEXT NOT NULL,
                    isAlive TEXT DEFAULT "#",
                    URL_TIME TEXT NOT NULL,
                    URL_TAG TEXT NOT NULL
                );
            '''
        )
        conn.commit()
        # print("xssdsd")
    except:
        # print("dsada")
        ...

# url 插入数据库
def url_table_insert(urls, url_tag):
    url_conn = sqlite3.connect("test.db")
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
            ...

    url_conn.close()


def url_table_read():
    url_conn = sqlite3.connect("test.db")
    url_c = url_conn.cursor()
    try:
        urls = url_c.execute('select * from URLS').fetchall()
        return urls
    except:
        ...
    finally:
        url_conn.close()

# 子域数据表检查
def subdomain_sql_check():
    conn = sqlite3.connect("test.db")
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
        console.print('子域数据表已存在', style="bold red")


# 插入SUBDOMAIN数据库
def insert_subdomain_sql(subdomains, tag):     # tag 每次收集打个标签方便区分
    subdomain_conn = sqlite3.connect("test.db")
    # console.print('数据库连接成功', style="#ADFF2F")
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
    subdomain_conn = sqlite3.connect("test.db")
    # console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        subdomains = subdomain_c.execute("select * from SUBDOMAIN").fetchall()
        return subdomains
    except:
        console.print('读取子域数据库失败', style="bold red")
    console.print('读取子域数据库成功', style="#ADFF2F")
    subdomain_conn.close()


def update_subdomain_sql(ip, cdn, domain):
    subdomain_conn = sqlite3.connect("test.db")
    # console.print('AUTOEARN数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        sql = "UPDATE SUBDOMAIN set IP='%s',CDN='%s' WHERE SUBDOMAIN='%s'" % (ip, cdn, domain)
        subdomain_c.execute(sql)
        # subdomain_c.execute("UPDATE SUBDOMAIN set IP=?,CND=? WHERE ID=?", (ip, cdn, id))
        subdomain_conn.commit()
    except:
        console.print('更新数据库失败', style="bold red")
    console.print("更新数据库成功", style="#ADFF2F")
    subdomain_conn.close()


# subdomain_sql_check()
domain_li = [
    'znjt.shenhuagroup.com.cn',
    'zhmmt.shenhuagroup.com.cn',
    'mobile.shenhuagroup.com.cn',
    'zt1.shenhuagroup.com.cn',
    'ghdl.shenhuagroup.com.cn',
    'dkgs.shenhuagroup.com.cn',
    'cwgs.shenhuagroup.com.cn',
    'hhgw.shenhuagroup.com.cn',
    'hwgs.shenhuagroup.com.cn',
    'shyjy.shenhuagroup.com.cn',
    'wzjt.shenhuagroup.com.cn',
    'xsjt.shenhuagroup.com.cn',
    'testvpnlp.shenhuagroup.com.cn',
    'tlhc.shenhuagroup.com.cn',
    'shtl.shenhuagroup.com.cn',
    'www.shenhuagroup.com.cn',
    'shwz.shenhuagroup.com.cn',
    'dns.shenhuagroup.com.cn',
    'xxgs.shenhuagroup.com.cn',
    'sxny.shenhuagroup.com.cn',
    'sdjt.shenhuagroup.com.cn',
    'nylt.shenhuagroup.com.cn',
    'nmgmjh.shenhuagroup.com.cn',
    'www.www.shenhuagroup.com.cn',
    'sslvpn.shenhuagroup.com.cn',
    'gjn.shenhuagroup.com.cn',
    'bstl.shenhuagroup.com.cn',
    'hjny.shenhuagroup.com.cn',
    'career.shenhuagroup.com.cn',
    'supplierdemo.shenhuagroup.com.cn',
    'swny.shenhuagroup.com.cn',
    'dns2.shenhuagroup.com.cn',
    'gsjt.shenhuagroup.com.cn',
    'ghtz.shenhuagroup.com.cn',
    'swfgs.shenhuagroup.com.cn',
    'wpu.shenhuagroup.com.cn',
    'dygl.shenhuagroup.com.cn',
    'dns1.shenhuagroup.com.cn',
    'gcgs.shenhuagroup.com.cn',
    'ysny.shenhuagroup.com.cn',
    'wwwlp.shenhuagroup.com.cn',
    'dns3.shenhuagroup.com.cn',
    'sdmt.shenhuagroup.com.cn',
    'snmy.shenhuagroup.com.cn',
    'mx.shenhuagroup.com.cn',
    'xjny.shenhuagroup.com.cn',
    'ec.sgeg.shenhuagroup.com.cn',
    'mail.shenhuagroup.com.cn',
    'sstl.shenhuagroup.com.cn',
    'sbny.shenhuagroup.com.cn',
    'sbgs.shenhuagroup.com.cn',
    'shcbs.shenhuagroup.com.cn',
    'wwwlp2.shenhuagroup.com.cn',
    'mzyhg.shenhuagroup.com.cn',
    'wpukfjj.shenhuagroup.com.cn',
    'supplier.shenhuagroup.com.cn',
    'whny.shenhuagroup.com.cn',
    'kjgs.shenhuagroup.com.cn',
    'wwwlp3.shenhuagroup.com.cn',
    'sdgs.shenhuagroup.com.cn',
    'tjmmt.shenhuagroup.com.cn',
    'hygs.shenhuagroup.com.cn',
    'ebuy.shenhuagroup.com.cn',
    'www.sgeg.shenhuagroup.com.cn',
    'dns.shenhuagroup.com.cn',
    'sdmt.shenhuagroup.com.cn',
    'bstl.shenhuagroup.com.cn',
    'shwz.shenhuagroup.com.cn',
    'supplier.shenhuagroup.com.cn',
    'hhgw.shenhuagroup.com.cn',
    'wwwlp.shenhuagroup.com.cn',
    'zt1.shenhuagroup.com.cn',
    'wzjt.shenhuagroup.com.cn',
    'dns1.shenhuagroup.com.cn',
    'wpu.shenhuagroup.com.cn',
    'tjmmt.shenhuagroup.com.cn',
    'nylt.shenhuagroup.com.cn',
    'whny.shenhuagroup.com.cn',
    'www.shenhuagroup.com.cn',
    'ghdl.shenhuagroup.com.cn',
    'snmy.shenhuagroup.com.cn',
    'xsjt.shenhuagroup.com.cn',
    'sbgs.shenhuagroup.com.cn',
    'sslvpn.shenhuagroup.com.cn',
    'ebuy.shenhuagroup.com.cn',
    'mzyhg.shenhuagroup.com.cn',
    'swfgs.shenhuagroup.com.cn',
    'xjny.shenhuagroup.com.cn',
    'dns2.shenhuagroup.com.cn',
    'www.sgeg.shenhuagroup.com.cn',
    'sdgs.shenhuagroup.com.cn',
    'sxny.shenhuagroup.com.cn',
    'www.www.shenhuagroup.com.cn',
    'wpukfjj.shenhuagroup.com.cn',
    'dygl.shenhuagroup.com.cn',
    'dns3.shenhuagroup.com.cn',
    'sstl.shenhuagroup.com.cn',
    'sbny.shenhuagroup.com.cn',
    'tlhc.shenhuagroup.com.cn',
    'shyjy.shenhuagroup.com.cn',
    'zhmmt.shenhuagroup.com.cn',
    'hjny.shenhuagroup.com.cn',
    'supplierdemo.shenhuagroup.com.cn',
    'shcbs.shenhuagroup.com.cn',
    'kjgs.shenhuagroup.com.cn',
    'ghtz.shenhuagroup.com.cn',
    'hygs.shenhuagroup.com.cn',
    'gsjt.shenhuagroup.com.cn',
    'dkgs.shenhuagroup.com.cn',
    'mobile.shenhuagroup.com.cn',
    'ec.sgeg.shenhuagroup.com.cn',
    'gjn.shenhuagroup.com.cn',
    'testvpnlp.shenhuagroup.com.cn',
    'wwwlp2.shenhuagroup.com.cn',
    'znjt.shenhuagroup.com.cn',
    'sdjt.shenhuagroup.com.cn',
    'nmgmjh.shenhuagroup.com.cn',
    'hwgs.shenhuagroup.com.cn',
    'ysny.shenhuagroup.com.cn',
    'wwwlp3.shenhuagroup.com.cn',
    'shtl.shenhuagroup.com.cn',
    'cwgs.shenhuagroup.com.cn',
    'career.shenhuagroup.com.cn',
    'xxgs.shenhuagroup.com.cn',
    'mx.shenhuagroup.com.cn',
    'swny.shenhuagroup.com.cn',
    'gcgs.shenhuagroup.com.cn',
    'mail.shenhuagroup.com.cn',
    'rbdp0htjbeta.shenhuagroup.cn',
    'rbdp0htj-repo.shenhuagroup.cn',
    'staging3g.shenhuagroup.cn',
    'sanantonio.shenhuagroup.cn',
    'mail0skins.shenhuagroup.cn',
    'pw.shenhuagroup.cn',
    'mail1.shenhuagroup.cn',
    'sharepoint.shenhuagroup.cn',
    'windows.shenhuagroup.cn',
    '12-mail0.shenhuagroup.cn',
    'mail10proxy.shenhuagroup.cn',
    'ws9.shenhuagroup.cn',
    'turmail0.shenhuagroup.cn',
    'betamail10.shenhuagroup.cn',
    'mail10node.shenhuagroup.cn',
    'mail8confluence.shenhuagroup.cn',
    'mail4pantheon.shenhuagroup.cn',
    'n-mail9.shenhuagroup.cn',
    'mail8.shenhuagroup.cn',
    'restrict-mail10.shenhuagroup.cn',
    'mail0-m.shenhuagroup.cn',
    'mail1server.shenhuagroup.cn',
    'machine-mail3.shenhuagroup.cn',
    'buckyabc1q2w3e4r5t.shenhuagroup.cn',
    'mail0.shenhuagroup.cn',
    'rbdp0htj-april.shenhuagroup.cn',
    'mail9devops.shenhuagroup.cn',
    'mail9-redirector.shenhuagroup.cn',
    'ns.shenhuagroup.cn',
    'mail10-stg.shenhuagroup.cn',
    'bn.shenhuagroup.cn',
    'mail9-latin.shenhuagroup.cn',
    'mail1c.shenhuagroup.cn',
    'dmin1.shenhuagroup.cn',
    'abc1q2w3e4r5t-engineering.shenhuagroup.cn',
    'mail9-backend.shenhuagroup.cn',
    'nl-mail9.shenhuagroup.cn',
    'hwabc1q2w3e4r5t.shenhuagroup.cn',
    'rbdp48htj.shenhuagroup.cn',
    'korea.shenhuagroup.cn',
    '3gsso.shenhuagroup.cn',
    '3mail10.shenhuagroup.cn',
    'mail3stage.shenhuagroup.cn',
    'internalmail3.shenhuagroup.cn',
    '19mail9.shenhuagroup.cn',
    'mail10.shenhuagroup.cn',
    'france.shenhuagroup.cn',
    'abc1q2w3e4r5ts3.shenhuagroup.cn',
    'restrictmail10.shenhuagroup.cn',
    'administrators.shenhuagroup.cn',
    'cust101.shenhuagroup.cn',
    'dev1abc1q2w3e4r5t.shenhuagroup.cn',
    'mail0-node.shenhuagroup.cn',
    'nalytics.shenhuagroup.cn',
    'rbdp0htj.shenhuagroup.cn',
    'accountsmail1.shenhuagroup.cn',
    'rbdp0htj-profile.shenhuagroup.cn',
    'machinerbdp0htj.shenhuagroup.cn',
    'march3g.shenhuagroup.cn',
    'mail9.shenhuagroup.cn',
    'mail10-euwe.shenhuagroup.cn',
    'firewallmail10.shenhuagroup.cn',
    'testbed-mail3.shenhuagroup.cn',
    'k-mail10.shenhuagroup.cn',
    'mail4.shenhuagroup.cn',
    'mail4-u.shenhuagroup.cn',
    'payroll.shenhuagroup.cn',
    'mail3o.shenhuagroup.cn',
    'mail1docker.shenhuagroup.cn',
    '3g.shenhuagroup.cn',
    'rbdp0htjcfg.shenhuagroup.cn',
    'mail1-system.shenhuagroup.cn',
    'mail10-u.shenhuagroup.cn',
    'mail10static.shenhuagroup.cn',
    'mail1cms.shenhuagroup.cn',
    'loadbalancer-mail3.shenhuagroup.cn',
    'p-mail9.shenhuagroup.cn',
    'datamail3.shenhuagroup.cn',
    'abc1q2w3e4r5telb.shenhuagroup.cn',
    'twitch-mail3.shenhuagroup.cn',
    'mail3v2.shenhuagroup.cn',
    'qamail3.shenhuagroup.cn',
    'cust26.shenhuagroup.cn',
    'mail8y.shenhuagroup.cn',
    'mail8brand.shenhuagroup.cn',
    'mail3.shenhuagroup.cn',
    'cmsrbdp0htj.shenhuagroup.cn',
    'h-mail1.shenhuagroup.cn',
    'mail4data.shenhuagroup.cn',
    'mail1engine.shenhuagroup.cn',
    'abc1q2w3e4r5tx.shenhuagroup.cn',
    '3-mail8.shenhuagroup.cn',
    'abc1q3w3e4r5t.shenhuagroup.cn',
    'mail1euw.shenhuagroup.cn',
    'abc32q2w3e4r5t.shenhuagroup.cn',
    'las-mail8.shenhuagroup.cn',
    'staff-mail4.shenhuagroup.cn',
    'engima-mail1.shenhuagroup.cn',
    'mail0bucket.shenhuagroup.cn',
    'euw-3g.shenhuagroup.cn',
    'twitch-mail10.shenhuagroup.cn',
    'mail4backend.shenhuagroup.cn',
    'mail0-westeurope.shenhuagroup.cn',
    'rbdp0htj-ssl.shenhuagroup.cn',
    'welcome.shenhuagroup.cn',
    'mail3fw.shenhuagroup.cn',
    'prd3g.shenhuagroup.cn',
    'abc1q2w3e4r5t-pay.shenhuagroup.cn',
    'u.shenhuagroup.cn',
    'mail0.shenhuagroup.cn',
    'rbdp0htj.shenhuagroup.cn',
    'restrict-mail10.shenhuagroup.cn',
    'mail1euw.shenhuagroup.cn',
    'firewallmail10.shenhuagroup.cn',
    'ws9.shenhuagroup.cn',
    'betamail10.shenhuagroup.cn',
    'abc1q2w3e4r5tx.shenhuagroup.cn',
    'machine-mail3.shenhuagroup.cn',
    '12-mail0.shenhuagroup.cn',
    'mail9devops.shenhuagroup.cn',
    'mail0skins.shenhuagroup.cn',
    'staff-mail4.shenhuagroup.cn',
    'k-mail10.shenhuagroup.cn',
    'mail9-backend.shenhuagroup.cn',
    'abc1q3w3e4r5t.shenhuagroup.cn',
    'mail3fw.shenhuagroup.cn',
    'rbdp0htj-profile.shenhuagroup.cn',
    'dmin1.shenhuagroup.cn',
    '19mail9.shenhuagroup.cn',
    'abc1q2w3e4r5ts3.shenhuagroup.cn',
    'cmsrbdp0htj.shenhuagroup.cn',
    'abc1q2w3e4r5t-pay.shenhuagroup.cn',
    'rbdp0htj-ssl.shenhuagroup.cn',
    'euw-3g.shenhuagroup.cn',
    'abc32q2w3e4r5t.shenhuagroup.cn',
    'administrators.shenhuagroup.cn',
    'mail8y.shenhuagroup.cn',
    'mail4data.shenhuagroup.cn',
    'windows.shenhuagroup.cn',
    '3gsso.shenhuagroup.cn',
    'bn.shenhuagroup.cn',
    'abc1q2w3e4r5t.shenhuagroup.cn',
    'mail1.shenhuagroup.cn',
    'mail3v2.shenhuagroup.cn',
    'buckyabc1q2w3e4r5t.shenhuagroup.cn',
    'accountsmail1.shenhuagroup.cn',
    'cust26.shenhuagroup.cn',
    'mail1-system.shenhuagroup.cn',
    'twitch-mail3.shenhuagroup.cn',
    'abc1q2w3e4r5t-engineering.shenhuagroup.cn',
    'rbdp48htj.shenhuagroup.cn',
    'n-mail9.shenhuagroup.cn',
    'mail9.shenhuagroup.cn',
    'dev1abc1q2w3e4r5t.shenhuagroup.cn',
    'mail8confluence.shenhuagroup.cn',
    'staging3g.shenhuagroup.cn',
    'p-mail9.shenhuagroup.cn',
    'las-mail8.shenhuagroup.cn',
    'prd3g.shenhuagroup.cn',
    'mail4.shenhuagroup.cn',
    '3-mail8.shenhuagroup.cn',
    'rbdp0htjbeta.shenhuagroup.cn',
    'france.shenhuagroup.cn',
    'mail10static.shenhuagroup.cn',
    'mail1c.shenhuagroup.cn',
    'h-mail1.shenhuagroup.cn',
    'pw.shenhuagroup.cn',
    'mail8.shenhuagroup.cn',
    'ns.shenhuagroup.cn',
    'march3g.shenhuagroup.cn',
    'internalmail3.shenhuagroup.cn',
    'mail4-u.shenhuagroup.cn',
    'mail9-latin.shenhuagroup.cn',
    'mail1engine.shenhuagroup.cn',
    'mail1server.shenhuagroup.cn',
    'sanantonio.shenhuagroup.cn',
    'mail10proxy.shenhuagroup.cn',
    'qamail3.shenhuagroup.cn',
    'datamail3.shenhuagroup.cn',
    'engima-mail1.shenhuagroup.cn',
    'mail4pantheon.shenhuagroup.cn',
    'welcome.shenhuagroup.cn',
    'mail3.shenhuagroup.cn',
    'rbdp0htj-repo.shenhuagroup.cn',
    'turmail0.shenhuagroup.cn',
    'cust101.shenhuagroup.cn',
    'abc1q2w3e4r5telb.shenhuagroup.cn',
    'sharepoint.shenhuagroup.cn',
    'mail0-node.shenhuagroup.cn',
    'restrictmail10.shenhuagroup.cn',
    'korea.shenhuagroup.cn',
    'mail8brand.shenhuagroup.cn',
    'hwabc1q2w3e4r5t.shenhuagroup.cn',
    'mail10-stg.shenhuagroup.cn',
    'mail10.shenhuagroup.cn',
    'mail1cms.shenhuagroup.cn',
    'rbdp0htjcfg.shenhuagroup.cn',
    'mail3o.shenhuagroup.cn',
    'mail4backend.shenhuagroup.cn',
    'u.shenhuagroup.cn',
    'mail10node.shenhuagroup.cn',
    'twitch-mail10.shenhuagroup.cn',
    'loadbalancer-mail3.shenhuagroup.cn',
    'machinerbdp0htj.shenhuagroup.cn',
    'nalytics.shenhuagroup.cn',
    'nl-mail9.shenhuagroup.cn',
    '3mail10.shenhuagroup.cn',
    'mail0-westeurope.shenhuagroup.cn',
    '3g.shenhuagroup.cn',
    'mail10-u.shenhuagroup.cn',
    'rbdp0htj-april.shenhuagroup.cn',
    'payroll.shenhuagroup.cn',
    'mail9-redirector.shenhuagroup.cn',
    'mail1docker.shenhuagroup.cn',
    'mail0-m.shenhuagroup.cn',
    'mail10-euwe.shenhuagroup.cn',
    'mail3stage.shenhuagroup.cn',
    'testbed-mail3.shenhuagroup.cn',
    'mail0bucket.shenhuagroup.cn',
    'lydl.chnenergy.com.cn',
    'pzny.chnenergy.com.cn',
    'slg.chnenergy.com.cn',
    'xstl.chnenergy.com.cn',
    'lygcjk.chnenergy.com.cn',
    'mobile.chnenergy.com.cn',
    'khjt.chnenergy.com.cn',
    'zhaopin.chnenergy.com.cn',
    'cydl.chnenergy.com.cn',
    'zbkg.chnenergy.com.cn',
    'lygc.chnenergy.com.cn',
    'pzmy.chnenergy.com.cn',
    'mail.chnenergy.com.cn',
    'wxpz.chnenergy.com.cn',
    'dygsyzg.chnenergy.com.cn',
    'www.chnenergy.com.cn',
    'lhdl.chnenergy.com.cn',
    'csie.chnenergy.com.cn',
    'nxdl.chnenergy.com.cn',
    'lyjs.chnenergy.com.cn',
    'mxsafe.chnenergy.com.cn',
    'wp.chnenergy.com.cn',
    'm.chnenergy.com.cn',
    'chnenergy.com.cn',
    'gnsdwt.chnenergy.com.cn',
    'gddl.chnenergy.com.cn',
    'cestri.chnenergy.com.cn',
    'henan.chnenergy.com.cn',
    'mhgpeixun.chnenergy.com.cn',
    'onlinestudy.chnenergy.com.cn',
    'robot.chnenergy.com.cn',
    'crm.chnenergy.com.cn',
    'sslvpn-lp.chnenergy.com.cn',
    'wpu.chnenergy.com.cn',
    'lhdlscp.chnenergy.com.cn',
    'gnsd.chnenergy.com.cn',
    'vpn.chnenergy.com.cn',
    'onlinestudytest.chnenergy.com.cn',
    'lygc.chnenergy.com.cn',
    'lygcjk.chnenergy.com.cn',
    'chnenergy.com.cn',
    'pzny.chnenergy.com.cn',
    'gddl.chnenergy.com.cn',
    'khjt.chnenergy.com.cn',
    'lyjs.chnenergy.com.cn',
    'www.chnenergy.com.cn',
    'mail.chnenergy.com.cn',
]

# url_table_create()
# insert_subdomain_sql(domain_li, "test")
# print(read_subdomain_sql())
# update_subdomain_sql("11111", "s1111", '3')
# print(read_subdomain_sql())
