from flask import Flask, request
from pusher import Pusher
from upload import save_file
from model import loadModel

app = Flask(__name__)

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
    result = loadModel("audio/file_1863_1684609878825.wav")
    label2int = {
        "-1": "negative",
        "0" : "neutral",
        "1" : "positive",
    }

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

    labelValue = {
        "-1": "negative",
        "0" : "neutral",
        "1" : "positive",
    }

    pusher.trigger("result-channel","show",labelValue[str(result)])

    return "done"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, threaded=True, debug=True)