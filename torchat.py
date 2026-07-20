from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime
import pytz

app=Flask(__name__)
socketio=SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    username=data['username']
    message = data['message']
    color = data['color']
    timestamp = datetime.now(pytz.utc).strftime('%m-%d %H:%M %Z')
    send({'username':username, 'message':message, 'color':color,'timestamp':timestamp},broadcast=True)

if __name__=='__main__':
    socketio.run(app,host='0.0.0.0', port=80, debug=True)