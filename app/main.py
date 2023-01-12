from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/index.html')



@socketio.on('mensageChat')
def chat(msg):
    print('mensaje: ' + msg)
    emit('emitirMensaje', msg, broadcast = True)
    
'''
@socketio.event
def my_event(message):
    emit('my event', {'data': 'got it!'})
'''            

if __name__ == '__main__': 
    socketio.run(app, debug=True, port=5300)