# flask initialization 
from flask import Flask, render_template,request, session ,redirect
# what is socekt-io?
# ans: Socket.IO is a library used for building real-time, bidirectional, and event-based communication between a client (typically a browser) and a server. It is commonly used in applications where real-time data updates are critical.


from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app=Flask(__name__)

app.config["SECRET_KEY"]='ajsdcnakjsdvaks'

socketio=SocketIO(app)

if __name__== '__main__':
    socketio.run(app,debug=True) # debug=true is for continues adapting the changes wihtout running the app agian again 
    
