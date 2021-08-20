from flask import Flask
from flask import request
from flask import jsonify
from providers.test_provider import Test_Provider
import json

app = Flask(__name__)
providers = (Test_Provider(),)

@app.route('/')
def root():
    return 'Backend is working'

@app.route('/info')
def info():
    names = list()
    for provider in providers:
        names.append(provider.name)
    return {'providers': names}

@app.route('/search')
def search():
    plugin = request.args.get('plugin')
    query = request.args.get('query')
    return 'test'

