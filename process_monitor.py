import time
import subprocess
from rich.console import Console
from lib import config
import os
from lib import file_op
from core.sql_helper import SQL_helper


def subdomain_status_check():
    console = Console()
    while True:
        cmd = "ps -aux | grep subfinder | grep -v grep | awk '{print $2}'"
        console.log('正在进行子域收集监控')
        start_rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(config.monitor_sleep_time)
        end_rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if len(start_rsp.stdout.read().strip()) != 0:
            console.log('子域收集中')
            if len(end_rsp.stdout.read().strip()) == 0:
                console.log('子域收集完成')
                break
    console.print("开始子域名入库……")
    # 入库完事后改掉文件名，前面加一个used
    try:
        sub_file_name = file_op.get_file_from_dir('./res/subdomain')
        target_file = ''
        for sub_file in sub_file_name:
            if 'used' in sub_file:
                print("ignore", sub_file)
            else:
                target_file = sub_file

        with open(target_file, 'r', encoding='utf-8') as f:
            subdomains = f.readlines()
            print(subdomains)
        SQL_helper.insert_subdomain_sql(subdomains)
        os.rename(target_file, './res/subdomain/used_' + target_file.split('/')[-1])
        console.log("子域名入库成功……")
    except Exception as e:
        console.log("子域名入库失败……")


if __name__ == '__main__':
    subdomain_status_check()
