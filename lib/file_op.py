# @Time    : 2022/4/12 16:07
# @Author  : Timer Zz
# @Email   : 2540373135@qq.com
import sys
from rich.console import Console
from lib import config
import os


def read_file_data():
    console = Console()
    data_list = []
    try:
        with open(config.domain_path, 'r', encoding="utf-8") as f:
            data = f.readlines()
        for line in data:
            data_list.append(line.strip())

        # print(data_list)
        return data_list
    except FileNotFoundError as e:
        console.print('目标文件读取异常，请检查文件是否存在', style="bold red")
        sys.exit()


def get_file_from_dir(d_path):
    file_list = []
    gx = os.walk(d_path)
    for N_path, N_dir_list, filelist in gx:
        for filename in filelist:
            file_list.append(N_path + '/' + filename)
    return file_list
