# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/10/30 18:39
'''

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 转换器：127.0.0.1:5000/goods/123
# @app.route('/goods/<int:goods_id>')
@app.route('/goods/<goods_id>',  methods=['GET']) # 如果不加转换器类型，默认是普通字符串规则（除了/的字符）
def goods_detail(goods_id):
    """定义的视图函数"""
    return f'goods detail page {goods_id}'

# 1.定义自己的转换器
class RegexConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则表达式
        self.regex = regex

# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter

# 127.0.0.1:5000/send/13213869866
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_message(mobile):
    return f'send message to {mobile}'


if __name__ == '__main__':
    # 通过url_map可以查看整个flask的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)
