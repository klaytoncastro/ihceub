import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Gere o site estático
os.system('pelican content')

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('./output', path)

@app.route('/')
def index():
    return send_from_directory('./output', 'index.html')

