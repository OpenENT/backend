from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/info')
def info():
    test = request.args.get('test')
    return 'test'

