from flask import Response, request
from application import app
from random import randint


@app.route('/routine/json', methods=['POST'])
def routine():
    task = request.get_json()
    toDo = task['taskData']
    routineNo = randint(0,(len(toDo)-1))
    routine = toDo[routineNo]
    return Response(routine, mimetype='text/plain')
