# flask template

from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    # return index.html
    return redirect(url_for('static', filename='index.html')) 

@app.route('/brute')
def traitor():
    # return traitor.html
    return redirect(url_for('static', filename='brute.html'))

if __name__ == '__main__':
    app.run(debug=True)
