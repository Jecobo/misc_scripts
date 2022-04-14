from socket import gethostbyname_ex
from queue import Queue
from threading import Thread
from core.sql_helper import SQL_helper
from rich.console import Console
import subprocess
import nmap

console = Console()


# 数据库域名转ip，检查cdn，插入数据库
class Domain2IP(Thread):
    def __init__(self, domain_queue):
        super(Domain2IP, self).__init__()
        self._domain_queue = domain_queue

    def run(self):
        while self._domain_queue.empty() is not True:
            domain = self._domain_queue.get()    # 拿到domain
            try:
                _res = gethostbyname_ex(domain)
                # print(f'domain:{_res[0]} , aliases:{_res[1]} , ip list:{_res[2]}')
                if len(_res[2]) != 1:
                    console.log(domain + 'cdn checked...')
                    # self._res_list.append([_res[0], ','.join(_res[1]), ','.join(_res[2])])
                    SQL_helper.update_subdomain_sql("cdn_checked", 'True', domain)
                else:
                    # self._res_list.append([_res[0], ','.join(_res[1]), ','.join(_res[2])])
                    # 更新ip，cdn字段
                    SQL_helper.update_subdomain_sql(_res[2][0], 'False', domain)
            except Exception as e:
                console.log("[error] 域名解析失败，不存活!")
            finally:
                self._domain_queue.task_done()     #


def ip_domain_cdn():
    domain_queue = Queue()
    # 读取数据库数据放入检查队列
    subdomains_list = SQL_helper.read_subdomain_sql()
    # print(subdomains_list)
    for sub_tuple in subdomains_list:
        # print(sub_tuple[1])
        domain_queue.put(sub_tuple[1])
    # 多线程调用解析域名
    for i in range(20):           # 线程 20
        a_thread = Domain2IP(domain_queue)
        a_thread.daemon = True
        a_thread.start()
    domain_queue.join()


def shodan_port_check():
    ...


def service_check(ip, port):
    url_list = []
    nm = nmap.PortScanner()
    ret = nm.scan(ip, port, arguments='-Pn,-sS')
    service_name = ret['scan'][ip]['tcp'][int(port)]['name']
    if 'http' in service_name or service_name == 'sun-answerbook':
        if service_name == 'https' or service_name == 'https-alt':
            url = 'https://' + ip + ':' + port
        else:
            url = 'http://' + ip + ':' + port

        return url


# masscan端口检测函数
def masscan_port_check(ip):
    tmp_list = []
    url_list = []
    results_list = []
    console.print('正在进行端口探测', style="#ADFF2F")
    # cmd = ['sudo', config.masscan_path, ip, '-p', config.masscan_port, '-oJ', config.masscan_file, '--rate', config.masscan_rate]
    cmd = 'sudo ' + config.masscan_path + " " + ip + ' -p ' + config.masscan_port + ' -oJ ' + config.masscan_file + ' --rate '+ config.masscan_rate
    rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        if rsp.poll() == None:    # poll() 返回none代表正在运行
            pass
        else:
            break
    with open(config.masscan_file, 'r') as wr:
        for line in json.loads(wr.read()):
            ip = line['ip']
            port = line['ports'][0]['port']
            result_dict = {
                'ip': ip,
                'port': port
            }
            tmp_list.append(result_dict)
        if len(tmp_list) > config.port_num_max:     # 端口过多直接pass
            tmp_list.clear()
        else:
            results_list.extend(tmp_list)
        for result in results_list:
            ip = result['ip']
            port = str(result['port'])
            url = service_check(ip, port)
            if len(url) > 0:
                url_list.append(url)
        # todo 做探活
        return url_list


def port_check():
    # todo 调用端口扫描，单独调用，多线程会被ban，网卡不行吃不消
    ...
