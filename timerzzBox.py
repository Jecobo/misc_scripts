# Time   ：2022/4/11 23:13
# Author : Timer Zz
# Email  : 2540373135@qq.com
from lib import banner
from core.auto_collect import subfinder
from rich.console import Console
import process_monitor
from core.auto_collect import port_scan
from core.auto_collect import httpx_alive
from lib import export_data


def main():
    console = Console()
    banner.banner()

    while True:
        console.print('请输入要执行的参数ID：[bold cyan]1-6[/bold cyan]', style="#ADFF2F")
        args = input('> ')
        if args == '1':
            subfinder.run_subfinder()
            # 监控子域名搜集情况
            process_monitor.subdomain_status_check()
            port_scan.ip_domain_cdn()     # 域名转ip 插入数据库
            port_scan.port_check()    # 端口扫描 结果入库
            httpx_alive.get_save_urls()    # 探活url存入数据库
            console.print("[info] auto info collect finish...", style='bold blue')
        elif args == '5':
            export_data.export_data()
        else:
            console.print('输入参数有误，请检查后输入', style="bold red")
            continue


if __name__ == '__main__':
    main()
