from flask import Flask, jsonify
import socket
import random

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/')
def index():
    # 模拟随机失败（测试熔断）
    if random.random() < 0.2:
        return jsonify({"error": "Service 2 failed"}), 503
    return jsonify({
        "status": "success",
        "message": "Hello from Service 2!",
        "server": hostname
    })

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  # 端口 8081