from flask import Flask, request,jsonify

app = Flask(__name__)    #创建flask对象app

# http://127.0.0.1:5000/index -> 执行index函数     GET是默认有的
# http://127.0.0.1:5000/index?age=19&pwd=123   浏览器输入
# 需要下载postman, 如果是post，会在请求体： xx=123&yy=999
#json 方式的请求体 : {"xx":123,"yy":999}
@app.route('/index',methods=["POST","GET"]) #可以接受POST进行访问
def index():

    #获取用户通过url传递过来的参数
    # age = request.args.get("age")
    # pwd = request.args.get("pwd")
    # print(age, pwd) #浏览器没输入age=19&pwd=123,终端会打 None None



    # 获取通过请求体传来的值,要下载postman伪造请求见笔记, post不会改变浏览器页面显示，刷新页面是用get
    # xx = request.form.get("xx")
    # yy = request.form.get("yy")
    # print(xx, yy)  #123 999

    print(request.json) #{"xx": 123, "yy": 999}
    print(request.json, type(request.json))  #{'xx': 123, 'yy': 999} <class 'dict'>
    data=request.json
    x = data.get("xx")
    y = data.get("yy")
    print(x,y) #123 999

    return jsonify({"status": "Lucky"}) #需要comment掉上面的才能展示,怪异
@app.route('/home')   # http://127.0.0.1:5000/home
def home():
    return "失败"

if __name__ == '__main__':

    # app.run()
    app.run(host='127.0.0.1', port=5000) #指定IP和端口