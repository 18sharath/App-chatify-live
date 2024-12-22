# flask initialization 
from flask import Flask, render_template,request, session ,redirect,url_for
# what is socekt-io?
# ans: Socket.IO is a library used for building real-time, bidirectional, and event-based communication between a client (typically a browser) and a server. It is commonly used in applications where real-time data updates are critical.


from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app=Flask(__name__)

app.config["SECRET_KEY"]='ajsdcnakjsdvaks'

socketio=SocketIO(app)

rooms={}
def generate_unique_code(length):
    while(True):
        code=""
        for _ in range(length):
            code=random.choice(ascii_uppercase)

        if code not in rooms:
            break
    return code




@app.route('/',methods=['POST','GET'])
def home():
    session.clear() 
    if request.method=='POST':
        name=request.form.get("name")
        join=request.form.get("join",False) # if we dont mention false here it will return none why we are writing is beacuse we can dirctly handled flase input 
        create=request.form.get("create",False)
        code=request.form.get("code")

        if not name:
            return render_template('home.html',error='please provide a name.')
        
        if join != False and not code  :# entry madidane but adu not correct in that time this will display
            return render_template('home.html',error='please provide a room code.')
        
        room=code
        if create!=False:
            room=generate_unique_code(4)
            rooms[room]={"members":0,"messages":[]} 
        elif code not in rooms:
            return render_template("home.html",error='room doesn\'t exist' )
        
        session[room]=room
        session[name]=name
        return redirect(url_for('room'))

    return render_template('home.html')

@app.route('/room')
def room():
    room=session.get('room')

    if room is None or session.get('name') is None  or room not in rooms:
        return redirect(url_for('home'))
    


    return render_template('room.html')

if __name__== '__main__':
    socketio.run(app,debug=True) # debug=true is for continues adapting the changes wihtout running the app agian again 

