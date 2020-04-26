from flask import render_template, redirect, url_for, request
from application import app
import requests




@app.route('/')

@app.route('/get/', methods = ['GET', 'POST'])
def home():
    task = requests.get('http://service2:5001/task/name')
    
    if task.text == 'exercise':
        time = requests.get('http://service3:5002/task/exercise')

    elif task.text == 'sing':
        time = requests.get('http://service3:5002/task/sing')

    elif task.text ==  'dance':
        time = requests.get('http://service3:5002/task/dance')

    routine = requests.post('http://service4:5003/routine', task=task.text, time=time.text)
    
    return render_template('home.html', title='Energise', task=task.text, time=time.text, routine=routine.txt)

