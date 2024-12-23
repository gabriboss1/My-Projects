from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from time import strftime
import socket

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

clients = []
usernames = {}
history = []

@socketio.on("set_username")
def username(data):
    usernames[request.sid] = data["username"]
    print(f"Username set for {request.sid}: {data['username']}")
    emit("chat_history", history, to=request.sid)

@socketio.on("connect")
def connect():
    clients.append(request.sid)
    print(f"Client {request.sid} has connected to the server.")

@socketio.on("disconnect")
def disconnect():
    username = usernames.get(request.sid, "Unknown")
    print(f"Client {request.sid} ({username}) has disconnected from the server.")
    if request.sid in clients:
        clients.remove(request.sid)
    if request.sid in usernames:
        del usernames[request.sid]

@socketio.on("message")
def message(data):
    time = strftime("%Y-%m-%d %H:%M:%S")
    username = usernames.get(request.sid, "Unknown")
    msg = {"username": username, "timestamp": time, "content": data['message']}
    history.append(msg)
    broadcast(msg)

def broadcast(message):
    for client_id in clients:
        emit("broadcast", message, to=client_id)

socketio.run(app, host=socket.gethostbyname(socket.gethostname()), debug=True, allow_unsafe_werkzeug=True)
