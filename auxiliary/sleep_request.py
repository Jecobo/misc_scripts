# @Time    : 2022/4/14 14:42
# @Author  : Timer Zz
# @Email   : 2540373135@qq.com

import requests
import time
from urllib import parse

with open("./springboot_path.txt", 'r', encoding="utf-8") as f:
    urls = f.readlines()

url = "http://lxxx/"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

for p in urls:
    x_url = parse.urljoin(url, p.strip())
    # print(x_url)
    try:
        resp = requests.get(url=x_url, headers=header)
        print(resp.status_code, x_url)
        time.sleep(2)
    except Exception as e:
        ...
