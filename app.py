from flask import Flask, request
from pusher import Pusher
import json
import os

app = Flask(__name__)

#Configure pusher
pusher = Pusher(
      app_id='1553130',
      key='28427b70b22ef2e1d217',
      secret='be23516479278dbb062c',
      cluster='us2',
      ssl=True
)

@app.route("/send")
def send_data():
    pusher.trigger("result-channel","show","success")
    return "done";

@app.route("/upload",methods = ['POST'])
def upload_data():
    if 'file' not in request.files:
        return "No File uploaded", 400
    file = request.files['file']
    if file.filename == "":
        return "No file selected", 400
    # Get the current directory
    current_dir = os.getcwd()
    audio_dir = os.path.join(current_dir,"audio")
    # Join the current directory with the filename
    file_path = os.path.join(audio_dir, file.filename)
    # Save the file to the specified path
    
    file.save(file_path)

    return 'File saved successfully'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, threaded=True, debug=True)