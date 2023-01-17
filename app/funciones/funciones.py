from conexion.conexionBD import * 
from datetime import date
from datetime import datetime


def listaMensajes(idUser, idSesion):
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    #$Msjs =("SELECT * FROM msjs WHERE (user_id ='" . $idConectado . "' AND to_id='" .$IdUser. "') OR (user_id='" .$IdUser. "' AND to_id='" . $idConectado . "') ORDER BY id ASC");
    querySQL  = ("SELECT * FROM mensajes WHERE (idUser='%s' AND idPara='%s') OR (idUser='%s' AND idPara='%s') ORDER BY idMensaje ASC" % (idSesion, idUser, idUser, idSesion,))
    print(querySQL)
    mycursor.execute(querySQL)
    mensajesUser = mycursor.fetchall() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return mensajesUser 


def listaDeContactosChats():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM users ORDER BY idUser DESC")
    mycursor.execute(querySQL)
    listaMisContactos = mycursor.fetchall() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return listaMisContactos 


def actualizarEstadoSesion(idUser='', estado =''):
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        mycursor         = conexion_MySQLdb.cursor(dictionary=True)
        
        tiempoActual    = datetime.now()
        fechaDesconexion = tiempoActual.strftime('%Y-%m-%d %H:%M:%S')
        print(fechaDesconexion)
        sql = mycursor.execute("""
            UPDATE users
            SET 
                estado   = %s,
                fecha_ultima_conexion = %s
            WHERE idUser = %s
            """, (estado, fechaDesconexion, idUser))
        conexion_MySQLdb.commit()
        
        mycursor.close() #cerrrando conexion SQL
        resultadoSQL = mycursor.rowcount #retorna 1 o 0
        return resultadoSQL
    
    
