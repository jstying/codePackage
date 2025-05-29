from flask import Flask, jsonify
import socket

app = Flask(__name__)
hostname = socket.gethostname()  # 获取本地主机名，标识不同实例

@app.route('/')
def index():
    return jsonify({
        "status": "success",
        "message": "Hello from Service 1!",
        "server": hostname
    })

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)  # 监听所有接口，端口 8082