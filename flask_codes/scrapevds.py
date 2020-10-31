import pafy
from flask_codes import app 

# url of video 
url= "succes"  ; 
# create video object
video = pafy.new(url)
# extract information about best resolution video available 
bestResolutionVideo = video.getbest()
list_videoQ=video.videostreams
list_audioQ=video.audiostreams




# download the video
bestResolutionVideo.download() 
