from application import app
from flask import request, Response
# function that picks random integers in type list (between 0 and 2)
from random import randint




@app.route('/task/exercise', methods = ['POST'])
def exercise_type():
    task = request.data.decode("utf-8")
    time = request.data.decode("utf-8")


    if task == "exercise":
        type= ['run', 'jump', 'stretch'] 
        return Response(type[randint(0,2)], mimetype='text/plain')

    if task == "sing":
        type= ['song1', 'song2','song3']
        return Response(type[randint(0,2)], mimetype='text/plain')
    
    if task == "dance":
        type= ['disco', 'ballroom','breakdance']
        return Response(type[randint(0,2)], mimetype='text/plain')








