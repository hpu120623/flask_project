# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/10/31 10:05
'''

from flask import Flask, jsonify, redirect, url_for

# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    """定义视图函数"""

    return 'hello flask'

# 通过methods限定访问方式
@app.route('/post_only', methods=['GET','POST'])
def post_only():
    return 'post only page'

@app.route('/hello', methods=['POST'])
# 如果路由重名，那么按照顺序来请求，可以改变请求方式
def hello():
    return 'hello 1'
#
@app.route('/hello',  methods=['GET'])
def hello2():
    return 'hello 2'


@app.route('/hi1')
@app.route('/hi2')
# 多个路由使用一个视图函数时
def hi():
    return 'hi page'


@app.route('/login')
def login():
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for('index')      # 使用url_for进行反解析
    return redirect(url)        # 跳转页面

@app.route('/register')
def register():
    url = url_for('index')
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看真个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)