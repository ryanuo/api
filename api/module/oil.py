import os
import time
import requests
from flask import jsonify

app_id = os.environ.get('OIL_APP_ID')
app_secret = os.environ.get('OIL_APP_SECRET')


def fetch_oil_price(province):
    api_url = 'https://www.mxnzp.com/api/oil/search'

    try:
        response = requests.get(f'{api_url}?province=${province}&app_id={app_id}&app_secret={app_secret}')
        response.raise_for_status()  # 如果请求不成功，会抛出异常
        return response.json().get('data')
    except requests.exceptions.RequestException as e:
        return {'error': 'fetch error data'}


def get_oil_price(data):
    results = []

    province = data.get('province')
    if isinstance(province, list):
        for i in province:
            if len(province) > 1:
                time.sleep(1)
            results.append(fetch_oil_price(i))

    return jsonify({'data': results, 'success': True})
