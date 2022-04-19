# @Time    : 2022/4/15 11:28
# @Author  : Timer Zz
# @Email   : 2540373135@qq.com
from core.sql_helper import SQL_helper
import httpx
from fake_useragent import UserAgent
import asyncio
import re
from rich.console import Console

ua = UserAgent()
title_pattern = r'<title>(.*?)</title>'
console = Console()


# 探活
async def requester(url):
    header = {
        "user-agent": ua.random,
    }
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url=url, headers=header)
            tmp = re.search(title_pattern, resp.text)
            if tmp:
                title = re.search(title_pattern, resp.text).group(1)
            else:
                title = "#"
            # 插入数据库
            SQL_helper.update_table_url(url, is_alive="True", status_code=str(resp.status_code), title=title)
        except:
            console.print("[error] no resp, target is not alive, pass it...", style='bold red')


def get_save_urls():
    urls_all = SQL_helper.url_table_read()
    for url_tuple in urls_all:
        url = url_tuple[1]
        asyncio.run(requester(url))


if __name__ == "__main__":
    get_save_urls()
