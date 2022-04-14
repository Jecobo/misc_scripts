from socket import gethostbyname_ex
from queue import Queue
from threading import Thread
from core.sql_helper import SQL_helper


# 数据库域名转ip，检查cdn，插入数据库
class Domain2IP(Thread):
    def __init__(self, domain_queue, res_list):
        super(Domain2IP, self).__init__()
        self._domain_queue = domain_queue
        self._res_list = res_list

    def run(self):
        while self._domain_queue.empty() is not True:
            domain = self._domain_queue.get()    # 拿到domain
            try:
                _res = gethostbyname_ex(domain)
                print(f'domain:{_res[0]} , aliases:{_res[1]} , ip list:{_res[2]}')
                self._res_list.append([_res[0], ','.join(_res[1]), ','.join(_res[2])])
            except Exception as e:
                print(e)
            finally:
                self._domain_queue.task_done()     #

        # return self._res_list


if __name__ == '__main__':
    res_list = []         # 存放结果的list
    domain_queue = Queue()

    # 读取数据库数据放入检查队列
    subdomains_list = SQL_helper.read_subdomain_sql()
    print(subdomains_list)
    for sub_tuple in subdomains_list:
        print(sub_tuple[1])
        domain_queue.put(sub_tuple[1])

    # 多线程调用解析域名
    for i in range(20):           # 线程 20
        a_thread = Domain2IP(domain_queue, res_list)
        a_thread.daemon = True
        a_thread.start()

    domain_queue.join()
