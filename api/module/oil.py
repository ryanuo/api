import requests

from api.module.common import api_request


def get_oil_price(data):
    province = data.get('province')

    # 替换成你的 API 调用逻辑
    api_url = 'https://www.mxnzp.com/api/oil/search'
    app_id = 'ngeorpqtkeijibqu'
    app_secret = 'ZWJlWXFzc21KNjYzVG9iakdBT3cydz09'

    # 构建 API 请求
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'province': province,
        'app_id': app_id,
        'app_secret': app_secret
    }

    # 发送 POST 请求
    response = requests.post(api_url, data=payload, headers=headers)
    return api_request(response)