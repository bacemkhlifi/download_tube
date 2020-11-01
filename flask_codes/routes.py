import pafy
from flask import  render_template,url_for,redirect,request

from flask_codes import app


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home')


@app.route('/succes',methods=["POST", "GET"])
def Succes():
    try : 
            
        if request.method == "POST" :
            succes = request.form['uname']

            # url of video 
            url=  request.form['uname'] 
            # create video object
            video = pafy.new(url)
            # extract information about best resolution video available 
            bestResolutionVideo = video.getbest()
            #list_videoQ=video.videostreams
            #list_audioQ=video.audiostreams
            # download the video
            bestResolutionVideo.download()
            return render_template('succes.html',title='Download',succes="https://www.youtube.com/embed/"+succes[32:43])
    except:
        print("<h1>url not valid</h1>")
        