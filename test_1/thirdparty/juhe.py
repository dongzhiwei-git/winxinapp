#!/usr/bin/python
# -*-encoding=utf8 -*-
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import os
import django
import json
import time
import requests

from utils import proxy


def constellation(cons_name):
    """
    :param cons_name: 星座名字
    :return: json 今天运势
    """
    key = '638590d043a54639f3560b5381f5c4f0'
    api = 'http://web.juhe.cn:8080/constellation/getAll'
    types = ('today', 'tomorrow', 'week', 'month', 'year')
    params = 'consName=%s&type=%s&key=%s' % (cons_name, types[0], key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    return {
        'name': cons_name,
        'text': data['summary']
    }


def stock(market, code):
    """
    沪深股票
    :param market: 上交所 = sh, 深交所 = sz
    :param code: 股票编号
    :return:
    """
    key = 'f887b09847c9bcde9801ca7aaa86513e'
    api = 'http://web.juhe.cn:8080/finance/stock/hs'
    params = 'gid=%s&key=%s' % (market + code, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    data = data.get('result')[0].get('data')
    response = {
        'name': data.get('name'),
        'now_price': data.get('nowPri'),
        'today_min': data.get('todayMin'),
        'today_max': data.get('todayMax'),
        'start_price': data.get('todayStartPri'),
        'date': data.get('date'),
        'time': data.get('time')
    }
    response['is_rising'] = data.get('nowPri') > data.get('todayStartPri')
    sub = abs(float(data.get('nowPri')) - float(data.get('todayStartPri')))  # 差值
    response['sub'] = float('%.3f' % sub)
    return response


def history_today():
    key = '6c6b318d983b6b4ac8cc5cda0da92155'
    api = 'http://api.juheapi.com/japi/toh'
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    params = 'v=1.0&month=%d&day=%d&key=%s' % (month, day, key)
    url = api + '?' + params
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    result_list = data.get('result')
    result = []
    for item in result_list:
        result.append({
            'title': item.get('title'),
            'content': item.get('des')
        })
    return result


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = 'd4ac90d0a7e5f2153ab36ffee16c2b71'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)
    result = json_data.get('result')
    sk = result.get('realtime')
    response = dict()
    response['temperature'] = sk.get('temperature')
    response['wind_direction'] = sk.get('direct')
    response['wind_strlength'] = sk.get('power')
    response['humidity'] = sk.get('humidity')

    print(response)

    # response = CommonWeatherResult()
    # # 温度

    return response


if __name__ == '__main__':
    data = weather('北京')
    print(data)
    pass
