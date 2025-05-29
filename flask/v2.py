from flask import Flask, request,jsonify
import hashlib
app = Flask(__name__)    #创建flask对象app


@app.route('/bili',methods=['POST']) #只接受POST进行访问
def bili():

    '''
    请求的数据格式要求  {"ordered_string":"..."}
    :return:
    '''

    #传给我orderedstring
    ordered_string = request.json.get('ordered_string')
    # 没有收到
    if not ordered_string:
        return jsonify({"status": False,'error':'参数错误'})



    #调用核心算法，生成sign签名
    encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign = obj.hexdigest()

    return jsonify({"status": True, "sign": sign})

if __name__ == '__main__':

    # app.run()
    app.run(host='127.0.0.1', port=5000) #指定IP和端口