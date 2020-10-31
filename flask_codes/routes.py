
from flask_codes import app
from flask import render_template ,url_for ,redirect ,request

@app.route('/')
@app.route('/Home')
def homepage():
    return render_template('homepage.html',title='Home')


@app.route('/succes',methods=["POST", "GET"])
def Succes():
    if request.method == "POST" :
        succes = request.form['uname']
        return render_template('succes.html',title='Download',succes="https://www.youtube.com/embed/"+succes[32:43])


