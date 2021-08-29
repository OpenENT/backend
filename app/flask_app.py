from flask import Flask
from flask import request
from flask import jsonify
from providers.test_provider import Test_Provider
from providers.youtube import YoutubeProvider
from providers.nicovideo import NicoProvider
import json

app = Flask(__name__)
providers = (Test_Provider(), YoutubeProvider(), NicoProvider())

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
    provider = request.args.get('provider')
    query = request.args.get('query')
    for p in providers:
        if provider in p.name:
            return {'response': 200, 'result': p.search(query=query)}
    return {'response': 404}
