from flask import Response, request
from application import app


@app.route('/routine/json', methods=['POST'])
def routine():
    task = request.get_json()
    task1 = task['task']
   # time = request.data.decode("utf-8")
    if task1 == 'exercise':
        routine = "Give us 10 push ups"
    elif task1 == 'sing':
        routine = "Sing the Beliver song by Imagine dragons"
    elif task1 == 'dance':
        routine = "Do the Macerena dance"
    else:
        routine = "No choices"
    return Response(routine, mimetype='text/plain')
