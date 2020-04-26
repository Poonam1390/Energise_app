from application import app
from flask import request, Response

# function that picks random integers in task list (between 0 and 2)
from random import randint


@app.route('/task/name', methods = ['GET'])
def task_name():
    tasks = ['exercise', 'sing', 'dance']
    return Response(tasks[randint(0,2)], mimetype='text/plain')


