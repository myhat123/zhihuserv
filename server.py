# -*- coding: utf8 -*-

import requests
import json
from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

@app.route('/zhihu/news/latest')
def get_zhihu_latest_news():
    url = "http://news-at.zhihu.com/api/4/news/latest"
    r = requests.get(url, headers=headers)

    return json.dumps(r.json(), ensure_ascii=False)

@app.route('/zhihu/news/<id>')
def get_zhihu_news(id):
    url = "http://news-at.zhihu.com/api/4/news/" + id
    r = requests.get(url, headers=headers)

    return json.dumps(r.json(), ensure_ascii=False)

@app.route('/zhihu/resource')
def get_resource():
    url = request.args.get('url')
    headers['Referer'] = 'https://daily.zhihu.com'
    r = requests.get(url, headers=headers, stream=True)

    rsp = make_response(r.raw.read())
    rsp.mimetype = "image/jpeg"

    return rsp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
