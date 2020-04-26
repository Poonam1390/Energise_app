from application import app
from flask import request, Response
# function that picks random integers in time list (between 0 and 2)
from random import randint


@app.route('/task/exercise', methods = ['POST'])
def exercise_time():
    task = request.data.decode("utf-8")
    time = ['5', '10', '15']
    return Response(time[randint(0,2)], mimetype='text/plain')

@app.route('/task/sing', methods = ['POST'])
def sing_time():
    task = request.data.decode("utf-8")
    time = ['2', '4', '8']
    return Response(time[randint(0,2)], mimetype='text/plain')

@app.route('/task/dance', methods = ['POST'])
def dance_time():
    task = request.data.decode("utf-8")
    time = ['5', '10', '20']
    return Response(time[randint(0,2)], mimetype='text/plain')

