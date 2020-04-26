import requests
from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Play
from application.forms import RoutineForm


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



@app.route('/addroutine', methods=['GET', 'POST'])
def addroutine():
    form = RoutineForm()
    if form.validate_on_submit():
        routineData = Play(
            exercise = form.exercise.data,
            sing = form.sing.data,
            dance = form.dance.data
        )

        db.session.add(routineData)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:
        print(form.errors)


    return render_template('addRoutine.html', title='AddingRoutine', form=form)


@app.route('/display')
def display():
    allData = Play.query.all()

    return render_template('display.html', title='Display' , routineData=allData)

