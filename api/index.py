import os

from flask import Flask, request
from flask_cors import CORS
from .module.oil import get_oil_price

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://ryanuo.cc"}})

app_id = os.environ.get('OIL_APP_ID')
app_secret = os.environ.get('OIL_APP_SECRET')


@app.route('/oil-price', methods=['POST'])
def oil_price():
    return get_oil_price(request.json)


@app.route("/", methods=["GET"])
def hello():
    get_oil_price({'province': ['河南']})
    return f"部署成功开始使用吧！{app_id}"
