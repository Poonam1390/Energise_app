import requests
from flask import render_template, redirect, url_for, request
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='HomePage')


@app.route('/routine')
def routine():
    task=requests.get('http://service2:5001/task/name')
    times=requests.post('http://service3:5002/times',data=task.text)
    routine=requests.post('http://service4:5003/routine/json',json={'task':task.text,'times':times.text})
    return render_template('routine.html',title='energise',task=task.text,times=times.text,routine=str(routine.text))
