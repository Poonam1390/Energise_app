from flask import request, Response
from application import app
from random import randint



@app.route('/task/name', methods=['GET'])
def task_name():
    tasks=['exercise', 'dance', 'sing']
    return Response(tasks[randint(0,2)], mimetype='text/plain')
