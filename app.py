import webbrowser
from flask import Flask,render_template,url_for,jsonify
import json

app=Flask(__name__)

@app.route('/index')
def index():
    d={"name": ["湖北", "香港", "台湾", "北京", "广东", "上海", "甘肃", "浙江", "福建", "澳门", "山东", "黑龙江", "陕西", "四川", "河北", "江苏", "辽宁", "广西", "云南", "江西", "河南", "海南", "天津", "重庆", "青海", "湖南", "山西", "宁夏", "安徽", "贵州", "吉林", "内蒙古", "西藏", "新疆"], "value": [67800, 273, 169, 514, 1407, 394, 134, 1237, 307, 19, 766, 484, 248, 543, 319, 633, 126, 254, 176, 936, 1273, 168, 137, 576, 18, 1018, 133, 75, 990, 146, 93, 75, 1, 76]}
    return render_template('visual_echarts.html',d=d)

if __name__=='__main__':
    app.run(debug=True)