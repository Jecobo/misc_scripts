# @Time    : 2022/4/14 16:33
# @Author  : Timer Zz
# @Email   : 2540373135@qq.com

from core.auto_collect import port_scan
import json
# port_scan.ip_domain_cdn()
# port_scan.port_check()

tmp_list = []
results_list = []
with open('masscan_test_res', 'r') as wr:  # 报错？
    # print(wr.read()[-4])
    str1 = wr.read()[:-4] + wr.read()[-3:] + ']'
    print(json.loads(str1))
    # for line in json.loads(wr.read()):
    #     ip = line['ip']
    #     port = line['ports'][0]['port']
    #     result_dict = {
    #         'ip': ip,
    #         'port': port
    #     }
    #     tmp_list.append(result_dict)

    # if len(tmp_list) > 50:  # 端口过多直接pass
    #     tmp_list.clear()
    # else:
    #     results_list.extend(tmp_list)
    # for result in results_list:
    #     ip = result['ip']
    #     port = str(result['port'])
    #     url = service_check(ip, port)
    #     if len(url) > 0:
    #         url_list.append(url)
    # # todo 做探活
    # return url_list