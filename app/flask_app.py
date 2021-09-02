from flask import Flask, send_from_directory, request, jsonify
from providers.youtube import YoutubeProvider
from providers.nicovideo import NicoProvider

import json

app = Flask(__name__, static_url_path='')
providers = (YoutubeProvider(), NicoProvider())

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

@app.route('/download')
def download():
    provider = request.args.get('provider')
    stream_url = request.args.get('stream_url')
    for p in providers:
        if provider in p.name:
            url = p.download(stream_url)
            if url is None:
                return {'response': 500}
            return {'response': 200, 'stream_url': f"http://127.0.0.1:5001/streams/{url}"}
    return {'response': 404}

@app.route('/streams/<path:path>')
def send_js(path):
    return send_from_directory('streams', path)
