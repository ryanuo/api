from flask import Flask, request
from flask_cors import CORS
from module.oil import get_oil_price

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://ryanuo.cc"}})


@app.route('/oil-price', methods=['POST'])
def oil_price():
    return get_oil_price(request.json)
