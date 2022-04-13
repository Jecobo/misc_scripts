# Time   ：2022/4/12 21:25
# Author : Timer Zz
# Email  : 2540373135@qq.com

from lib import file_op
from core.sql_helper import SQL_helper
import os


sub_file_name = file_op.get_file_from_dir('./res/subdomain')   # file list
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
