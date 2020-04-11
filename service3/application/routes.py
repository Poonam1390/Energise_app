from flask import request, Response
from application import app
from random import randint


@app.route('/times', methods=['POST'])
def times():
    task = request.data.decode("utf-8")
    exercise = [10,15,20]
    sing = [2,3,4]
    dance = [3,4,5]
    if task == 'exercise':
        duration = exercise[randint(0,2)]
    elif task == 'sing':
        duration = sing[randint(0,2)]
    elif task == 'dance':
        duration = dance[randint(0,2)]
    else:
        duration = 0
    return Response(str(duration), mimetype='text/plain')
