# Time   ：2022/4/11 21:36
# Author : Timer Zz
# Email  : 2540373135@qq.com

import time
from rich.console import Console
from rich.table import Column, Table


# banner生成函数
def banner():
    console = Console()
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
    table.add_column("ABOUT", style="dim", width=35)
    table.add_column("AUTHOR", style="dim", width=25)
    table.add_column("PLUGINS", style="dim", width=30)
    help_table = Table(show_header=True, header_style="bold magenta")
    help_table.add_column("ID", style="dim", width=30)
    help_table.add_column("参数", style="dim", width=30)
    help_table.add_column("说明", style="dim", width=30)
    table.add_row(
        "我很懒老想着程序帮我完成一些事情",
        "timerzz",
        ""
    )
    table.add_row(
        "",
        "",
        ""
    )
    table.add_row(
        "",
        "",
        ""
    )
    table.add_row(
        "",
        "",
        ""
    )
    table.add_row(
        "",
        "",
        ""
    )
    table.add_row(
        "",
        "",
        ""
    )
    help_table.add_row(
        "1",
        "auto info collect",
        "自动化信息搜集"
    )
    help_table.add_row(
        "2",
        "auto vul scan",
        "自动化漏扫"
    )
    help_table.add_row(
        "3",
        "all in",
        "一把梭"
    )
    help_table.add_row(
        "4",
        "confused",
        "我很迷茫"
    )
    help_table.add_row(
        "5",
        "export",
        "导出"
    )
    help_table.add_row(
        "6",
        "Exit",
        "退出"
    )

    console.print(table)
    console.print(help_table)


# banner()
