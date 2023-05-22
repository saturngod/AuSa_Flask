from flask import Flask, request
from pusher import Pusher
from upload import save_file
from model import loadModel

app = Flask(__name__)

label2int = {
        "0": "negative",
        "1" : "neutral",
        "2" : "positive",
}

#Configure pusher
pusher = Pusher(
      app_id='1553130',
      key='28427b70b22ef2e1d217',
      secret='be23516479278dbb062c',
      cluster='us2',
      ssl=True
)

@app.route("/load")
def load_data():
    result = loadModel("audio/109.wav")
    
    
    return label2int[str(result)];

@app.route("/send")
def send_data():
    pusher.trigger("result-channel","show","Male, Postive")
    return "done";

@app.route("/upload",methods = ['POST'])
def upload_data():
    if 'file' not in request.files:
        return "No File uploaded", 400
    file = request.files['file']
    if file.filename == "":
        return "No file selected", 400
    
    wav_file = save_file(file)

    result = loadModel(wav_file)

    pusher.trigger("result-channel","show",label2int[str(result)])

    return "done"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, threaded=True, debug=True)