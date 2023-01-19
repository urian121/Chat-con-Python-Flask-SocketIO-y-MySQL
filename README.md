# PASO 1, Crear mi entorno virtual
```python3 -m venv env ```

# PASO 2, Activar el entorno virtual ejecutando;
``` . env/Scripts/activate ```
 
# PASO 3, Ya dentro del entorno virtual instalar flask
``` pip install flask ```

# PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para conectar Python con MySQL
``` pip install mysql-connector-python ```

# nstalar Flask-SocketIO: Puedes instalar Flask-SocketIO utilizando el administrador de paquetes de Python pip ejecutando el siguiente comando en tu terminal: pip install flask-socketio
``` pip install flask-socketio ```

# Instalar Modulo OpenCV, para redimensionar imagenes
``` pip install opencv-contrib-python ```

# PASO 5, Lista todos mis paquetes
``` pip list  o pip freeze ```

# Crear/Actualizar el fichero requirements.txt:
``` pip freeze > requirements.txt ```

# (env)$ deactivate   Para desactivar nuestro entono virtual
 
# Comando para actualizar pip:
``` python -m pip install --upgrade pip ```
# Link de Referencia 
``` https://pypi.org/project/Flask-SocketIO/ ```
``` https://flask-socketio.readthedocs.io/en/latest/index.html```
``` https://pypi.org/project/Pillow/  ```



# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo
# requirements.txt con el comando;
``` pip install -r requirements.txt ```
# en el mismo se encuentran todas las dependecias del proyecto.

# Nota: cuando valla hacer una actualizacion del archivo requirements.txt debo estar
# dentro de mi entorno virtual pero no dentro de la carpera app solo en mi entorno.

# chat-list-content.html
{
    onclick="seleccionarUsuario('{{ contacto.idUser }}');"
}
->BaeHome.html ->JavaScript ->ajax ->seleccionarUsuario
->main.py ->recibo el id del usuario seleccionado y lo envio a la funcion listaMensajes(idUserSeleccionado, idUserSesion) enviando tambien el id del usuario en session.

->La funcion (idUserSeleccionado, idUserSesion) que esta en el archivo de funciones,
  consulta todos los chats tanto enviados como recibidos por ambas partes retornando los mismos.

->Desade esta funcion seleccionarUsuario que esta en main.py, envio chat-body.html el id que fue seleccionado, los mensajes entre ambos y los datos de la session.

-> En el archivo chat-body.html muestro todos los chats entre el usuario seleccionado con        respecto al usuario en sesion.

-> Luego como he enviado el idSeleccionado al archivo  chat-body.html con JavaScript desde el baseHome.html selecciono dicho id cuando envio el formulario, con el fin de determinar para quien es el mensajes.

-> Envio el mensaje al socket 'mensajeChat' donde inserto el mensaje en BD y consulto la funcion
listaMensajes(idSeleccionado, idUserSesion) la mismo como se comento antes, consulta todos los chats entre ambas partes, es decir mostra los mensajes enviados entre ambas partes.


-> mostrarMensajes(data) es una funcion que envia el mensaje a la vista de 'mensajesChat' pero primero va ha mensajesChat() que esta en main.py

-> funciones.py ->def listaMensajes(idUser, idSesion):