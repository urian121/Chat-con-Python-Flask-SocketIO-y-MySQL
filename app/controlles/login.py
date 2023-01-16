from flask import request, render_template, session, redirect, url_for
from conexion.conexionBD import * 
from funciones.funciones import *



import re
from werkzeug.security import generate_password_hash, check_password_hash



def informacionSesion():
    informLogin = {
        "idUser"              :session['idUser'],
        "primer_nombre"       :session['primer_nombre'],
        "email_cliente"       :session['email_cliente'],
        "estado"              :session['estado']
    }
    return informLogin


def verificarLogin(email_cliente='', password_cliente=''):
    email_cliente      = (request.form['email_cliente'])
    password_cliente   = (request.form['password_cliente'])
    
    conexion_MySQLdb = connectionBD() 
    cursor           = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("""SELECT
                        idUser,
                        email_cliente,
                        password_cliente, 
                        primer_nombre,
                        estado
                    FROM users 
                    WHERE email_cliente = %s""", (email_cliente,))
    filaResultado = cursor.fetchone()
    if filaResultado:
        msg =''
        if check_password_hash(filaResultado['password_cliente'], password_cliente):
            session['conectado']        = True
            session['idUser']           = filaResultado['idUser']
            session['primer_nombre']    = filaResultado['primer_nombre']
            session['email_cliente']    = filaResultado['email_cliente']
            session['estado']           = filaResultado['estado']
            
            #Cambio el estado de la Sesión
            respuesta    = actualizarEstadoSesion(session['idUser'], 1)
            if(respuesta == 1):
                msg = "Proceso completado con éxito."
                return render_template('public/home.html',  dataLogin = informacionSesion(), misContactos = listaDeContactosChats())                  
        else:
            #La cuenta no existe o el nombre de usuario/contraseña es incorrecto
            msg = 'Correo electrónico/contraseña incorrectos.'
            return render_template('public/login/login.html', msg_alerta = msg)     
    elif request.method == 'POST':
        msg = '¡Por favor rellena el formulario!'
    return render_template('public/login/login.html', msg=msg)
    
 
 
def crearCuentaUsuario(primer_nombre ='', email_cliente ='', password_cliente =''):
    primer_nombre               = request.form['primer_nombre']
    email_cliente               = request.form['email_cliente']
    password_cliente            = request.form['password_cliente']
    
    
    # Comprobar si existe una cuenta usando MySQL, con respecto al email
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE email_cliente = %s', (email_cliente,))
    filaResultado = cursor.fetchone()
    cursor.close() #cerrrando conexion SQL
        
    # Si la cuenta existe, muestra los controles de error y validación.
    if filaResultado:
        msg = 'Ya existe la cuenta'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email_cliente):
        msg = 'Correo no valido!'
    elif not email_cliente or not password_cliente or not password_cliente:
        msg = 'Por favor llene todos los campos!'
    else:
        # La cuenta no existe y los datos del formulario son válidos,
        nueva_password = generate_password_hash(password_cliente, method='sha256')
        
        
        conexion_MySQLdb = connectionBD()
        cursor      = conexion_MySQLdb.cursor(dictionary=True)
        
        sql         = ("INSERT INTO users ( primer_nombre, email_cliente, password_cliente, estado) VALUES (%s, %s, %s, %s)")
        valores     = (primer_nombre, email_cliente, nueva_password, 0)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close()
        #conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Cuenta creada correctamente'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
    return render_template('public/login/login.html')



def verificaSesion():
    if 'conectado' in session:
        return render_template('public/home.html', dataLogin = informacionSesion())
    else:
        return render_template('public/login/login.html')    
    
    
def cerrarLogin():
    if request.method == 'GET':
        respuesta = actualizarEstadoSesion(session['idUser'], 0)
        if(respuesta == 1):
            msgClose = ''
            session.pop('conectado', None)
            session.pop('idUser', None)
            session.pop('email_cliente', None)
            msgClose ="Sesión cerrada con éxito"
            return redirect(url_for('inicio'))
        else:
            msg = ''
            return render_template('public/home.html', msg='No se pudo cerrar la sesión')
    else:
        return render_template('public/home.html')