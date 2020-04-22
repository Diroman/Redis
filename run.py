"""
Database struct
logN(hash-key) time(key) time-value url(key) url-value ip(key) ip-value
"""
import connect
import time
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def write_log():
    if request.path == '/favicon.ico':
        return
    connect.add_log(time.time(), request.path, request.remote_addr)


@app.route('/')
def home():
    return 'OK'


@app.route('/logs')
def show_log():
    logs = connect.get_logs()
    return render_template('logs.html', rows=logs)


@app.route('/<string:path>')
def another_url(path):
    print(f"Get request on {path}")
    return path


if __name__ == "__main__":
    try:
        with open("config.json") as f:
            config = json.load(f)
        connect.init_connection(host=config['host'], port=config['port'])
        app.run(host="localhost", port=5000)
    finally:
        connect.clear_base()
