import sqlite3
from lib import config
from flask import Flask, request
from flask_paginate import Pagination
from flask import render_template

app = Flask(__name__)
DATABASE = config.result_sql_path


@app.route('/')
def index():
    # 获取子域数据
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    sql = "SELECT * FROM SUBDOMAIN"
    cur.execute(sql)
    subdomains = cur.fetchall()
    # ？
    plugin_list = []
    s = set()
    result_list = []
    for plugins in plugin_list:
        if plugins not in s:
            s.add(plugins)
            result = {
                'name': plugins,
                'value': plugin_list.count(plugins)
            }
            result_list.append(result)

    # 分页
    PER_PAGE = config.PER_PAGE #每页展示条数
    total = len(subdomains)
    page = int(request.args.get('page', 1))
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginate = Pagination(bs_version=4, page=page, total=total, per_page=PER_PAGE)
    subdomain = subdomains[start:end]
    return render_template('index.html', paginate=paginate, subdomain=subdomain, result_list=result_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)
