from flask import jsonify


def api_request(response):
    """
    处理 API 请求的函数
    :param response: API 请求的响应对象
    :return: 处理后的响应数据
    """
    if response.status_code == 200:
        # 返回 API 的响应数据
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'})
