# Time   ：2022/4/11 23:13
# Author : Timer Zz
# Email  : 2540373135@qq.com
from lib import banner, file_op
from core.auto_collect import subfinder
from rich.console import Console
import sys
from core.sql_helper import SQL_helper

# SQL_helper.subdomain_sql_check()


def main():
    console = Console()
    banner.banner()
    while True:
        console.print('请输入要执行的参数ID：[bold cyan]1-6[/bold cyan]', style="#ADFF2F")
        args = input('> ')
        if args == '1':
            # domains = read_file.read_file_data()   # 读取文件
            # for domain in domains:
            subfinder.run_subfinder()
        else:
            console.print('输入参数有误，请检查后输入', style="bold red")
            sys.exit()


if __name__ == '__main__':
    main()
