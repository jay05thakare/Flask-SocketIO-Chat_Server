from math import fabs
from flask  import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
  print('Message: ' + msg)
  send('Message: ' + msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
    app.run(debug=False, host='0.0.0.0')