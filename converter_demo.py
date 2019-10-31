# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/10/31 10:05
'''

from flask import Flask, jsonify, redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)


# 转换器
# 127.0.0.1:5000/goods/123
# @app.route('/goods/<int:goods_id>')
@app.route('/goods/<goods_id>')  # 不加转换器类型，默认是普通字符串类型（除了/的字符）
def goods_detail(goods_id):
    """定义视图函数"""
    return 'goods detail page %s' % goods_id


# 1.定义自己的转换器
class RegexConverter(BaseConverter):
    """
    继承BaseConverter
    """
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        print('to_python方法被调用')
        # return '110'
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        # 使用url_for的方法的时候被调用
        return '13022222222'


# # 2.将自定义的转换器添加到flask的应用中
app.url_map.converters['re'] = RegexConverter


# 3.使用
# 127.0.0.1::5000/send/13312345678
@app.route('/send/<re(r"1[34578]\d{9}"):mobile>')
def send_sms(mobile):
    return 'send sms to %s' % mobile

@app.route('/index')
def index():
    url = url_for('send_sms', mobile='13012345678')
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看真个flask中的路由信息
    # print(app.url_map)
    # 启动flask程序
    app.run(debug=True)
