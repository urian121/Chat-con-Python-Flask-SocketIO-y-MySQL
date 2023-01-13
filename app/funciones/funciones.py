from flask import render_template, session
from conexion.conexionBD import * 



def listaMensages(idUser):
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM mensajes WHERE idUser='%s'" % (idUser,))
    mycursor.execute(querySQL)
    mensajesUser = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return mensajesUser 



def linkCrearCuentaUsuario():
    if 'conectado' in session:
        return render_template('public/index.html')
    else:
        return render_template('public/login/crearCuenta.html')
    
    
