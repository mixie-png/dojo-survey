from flask import render_template, redirect, request, url_for, session
from flask_app import app
from flask_app.models.survey import Survey

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if not Survey.validate_survey(request.form):
        return redirect('/')

    # after successful creation of a new Survey, redirect to Result page and display the NEW information
    return redirect(url_for('result', survey_id = Survey.add(request.form)))
    # return redirect('/result')


@app.route('/result/<int:survey_id>')
def result(survey_id):
    # calling the get_one method and supplying it with the id of the user we want to get
    survey = Survey.show_one(survey_id)
    # passing one user to our template so we can display them
    return render_template("result.html", one_survey = survey)