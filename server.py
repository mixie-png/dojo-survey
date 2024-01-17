from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'can you keep a secret?'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['frontend'] = request.form['frontend']
    session['feelings'] = request.form['feelings']
    session['comment'] = request.form['comment']
    print(session['name'])
    print(session['location'])
    print(session['language'])
    print(session['frontend'])
    print(session['feelings'])
    print(session['comment'])
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html',
    name = session['name'],
    location = session['location'],
    language = session['language'],
    frontend = session['frontend'],
    feelings = session['feelings'],
    comment = session['comment']
    )






if __name__ == "__main__":
    app.run(debug=True)