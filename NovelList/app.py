from flask import Flask, render_template, request, redirect, url_for, session, flash, current_app, g

app = Flask(__name__)

indexVariables = {
    'title': 'Baza danych Novelek',
    'heading': 'Novelki'
}

@app.route('/')
def index():
    return render_template('index.html', **indexVariables)
    # return('testing')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('createform.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')