import time
import subprocess
from rich.console import Console
from lib import config


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


if __name__ == '__main__':
    subdomain_status_check()
