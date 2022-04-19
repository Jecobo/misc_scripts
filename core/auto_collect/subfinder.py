# Time   ：2022/4/11 22:00
# Author : Timer Zz
# Email  : 2540373135@qq.com

from subprocess import PIPE, Popen
from rich.console import Console
import time
from lib import config

now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())


def run_subfinder():
    console = Console()
    cmdx = 'nohup subfinder -silent -dL ' + config.domain_path + ' -o ./tmp/subdomain/' + now_time + ' 2>&1'
    console.print("[bold blue][info] exec: " + cmdx + '[/bold blue]')
    try:
        proc = Popen(
            cmdx,
            stdin=None,  # 标准输入 键盘
            stdout=PIPE,  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
            stderr=PIPE,  # 标准错误，保存到管道
            shell=True
        )
        # console.print("正在进行子域收集:", style="#ADFF2F")
    except Exception as e:
        console.print("[error] subfinder 运行失败!", style="bold red")
