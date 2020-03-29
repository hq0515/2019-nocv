from data import get_data
from flask import Flask,render_template,url_for,jsonify
import json

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/China')
def view_china():
    time=get_data.get_time()
    data=get_data.get_data_china()
    return render_template('China.html',d=data,today=time)

@app.route('/World')
def view_world():
    time=get_data.get_time()
    data=get_data.get_data_world()
    return render_template('World.html',d=data,today=time)

if __name__=='__main__':
	app.run(debug=True)