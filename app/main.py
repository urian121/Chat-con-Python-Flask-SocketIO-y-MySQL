from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import uuid


from conexion.conexionBD import * #Conexión para la BD
from controlles.login import * #Información para toda la gestión login
from funciones.funciones import * #Mis funciones 
from routers.routes import *



#Importando SocketIO desde flask_socketio
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chat*secret2023*!'
socketio = SocketIO(app)



@app.route('/login', methods=['GET','POST'])
def inicio():
    return verificaSesion()
    


@app.route('/Home', methods=['GET', 'POST'])
def login():
    if 'conectado' in session:
        return render_template('public/home.html',  dataLogin = informacionSesion())  
    else:
        if request.method == 'POST' and 'email_cliente' in request.form and 'password_cliente' in request.form:
            return verificarLogin(request.form['email_cliente'], request.form['password_cliente'])   
        else:
            return render_template('public/login/login.html')



@socketio.on('mensajeChat')
def chat(msg, idUser):       
    
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    
    sql  = ("INSERT INTO mensajes ( idUser, idPara, mensaje) VALUES (%s, %s, %s)")
    valores     = (idUser, 2, msg)
    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    cursor.close()#cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
            
    #print('mensajdasdasde: ' + msg)
    resultMensajes = listaMensajes(idUser)
    emit('emitirMensaje', str(resultMensajes), broadcast = True)


@app.route('/mensages-chat', methods=['GET','POST'])
def mensajesChat():
    listaMsgsChat = request.json['msgs_chat']
    return render_template('public/dashboard/chat-body.html', miDataMsgs = listaMsgsChat, dataLogin = informacionSesion())
    
    

@app.route('/crear-mi-cuenta', methods=['GET', 'POST'])
def fromCrearCuentaUsuario():
    if request.method == 'POST' and 'primer_nombre' in request.form and 'email_cliente' in request.form and 'password_cliente' in request.form:
        return crearCuentaUsuario(request.form['primer_nombre'], request.form['email_cliente'], request.form['password_cliente'])
    else:
        return render_template('public/index.html')
    



@app.route('/view-crear-mi-cuenta-usuario', methods=['GET'])
def linkCrearCuentaUsuario():
    return viewCrearCuentaUsuario()
    
    

@app.route('/view-recuperar-mi-cuenta', methods=['GET','POST'])
def recuperarMiCuentaUsuario():
    return linkrecuperarMiCuentaUsuario()
    


@app.route('/salir', methods=['GET'])
def cerrarSesion():
    return cerrarLogin()



@app.errorhandler(404)
def pagina_no_encontrada(error):
    return verificaSesion()
    
    
    
if __name__ == '__main__': 
    socketio.run(app, debug=True, port=5300)