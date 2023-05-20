from flask import Flask, request
from pusher import Pusher
from upload import save_file

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
    pusher.trigger("result-channel","show","Female, Postive")
    return "done";

@app.route("/upload",methods = ['POST'])
def upload_data():
    if 'file' not in request.files:
        return "No File uploaded", 400
    file = request.files['file']
    if file.filename == "":
        return "No file selected", 400
    
    save_file(file)

    return 'File saved successfully'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, threaded=True, debug=True)