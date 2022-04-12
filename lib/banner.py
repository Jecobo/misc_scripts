# Time   ：2022/4/11 21:36
# Author : Timer Zz
# Email  : 2540373135@qq.com

import time
from rich.console import Console
from rich.table import Column, Table

console = Console()

# banner生成函数
def banner():
    msg = '''
       /$$     /$$                                                             /$$                          
      | $$    |__/                                                            | $$                          
     /$$$$$$   /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$      | $$$$$$$   /$$$$$$  /$$   /$$
    |_  $$_/  | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$|____ /$$/|____ /$$/      | $$__  $$ /$$__  $$|  $$ /$$/
      | $$    | $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/   /$$$$/    /$$$$/       | $$  \ $$| $$  \ $$ \  $$$$/ 
      | $$ /$$| $$| $$ | $$ | $$| $$_____/| $$        /$$__/    /$$__/        | $$  | $$| $$  | $$  >$$  $$ 
      |  $$$$/| $$| $$ | $$ | $$|  $$$$$$$| $$       /$$$$$$$$ /$$$$$$$$      | $$$$$$$/|  $$$$$$/ /$$/\  $$
       \___/  |__/|__/ |__/ |__/ \_______/|__/      |________/|________/      |_______/  \______/ |__/  \__/
    '''

    console.print(msg, style="bold red")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ABOUT", style="dim", width=30)
    table.add_column("AUTHOR", style="dim", width=30)
    table.add_column("PLUGINS", style="dim", width=30)
    help_table = Table(show_header=True, header_style="bold magenta")
    help_table.add_column("ID", style="dim", width=30)
    help_table.add_column("参数", style="dim", width=30)
    help_table.add_column("说明", style="dim", width=30)
    table.add_row(
        "一款SRC漏洞挖掘辅助工具",
        "Echocipher",
        "OneForAll"
    )
    table.add_row(
        "",
        "",
        "Masscan"
    )
    table.add_row(
        "",
        "",
        "Nmap"
    )
    table.add_row(
        "",
        "",
        "Wafw00f"
    )
    table.add_row(
        "",
        "",
        "Crawlergo"
    )
    table.add_row(
        "",
        "",
        "Xray"
    )
    help_table.add_row(
        "1",
        "Subdomain_Collect",
        "获取子域"
    )
    help_table.add_row(
        "2",
        "Port_Check",
        "端口检测"
    )
    help_table.add_row(
        "3",
        "Waf_Check",
        "WAF检测"
    )
    help_table.add_row(
        "4",
        "Craw_To_Xray",
        "爬虫爬取 + 漏洞探测 + 消息通知"
    )
    help_table.add_row(
        "5",
        "View",
        "查看"
    )
    help_table.add_row(
        "6",
        "Exit",
        "退出"
    )
    console.print(table)
    console.print('参数说明', style="#ADFF2F")
    console.print(help_table)


banner()
