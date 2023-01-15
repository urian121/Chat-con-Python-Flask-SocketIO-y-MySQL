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
# PASO 5, Lista todos mis paquetes
``` pip list  o pip freeze ```

# Crear/Actualizar el fichero requirements.txt:
``` pip freeze > requirements.txt ```

# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo
# requirements.txt con el comando;
``` pip install -r requirements.txt ```
# en el mismo se encuentran todas las dependecias del proyecto.

# Instalar Modulo OpenCV, para redimensionar imagenes
``` pip install opencv-contrib-python ```
# (env)$ deactivate   Para desactivar nuestro entono virtual
 
# Comando para actualizar pip:
``` python -m pip install --upgrade pip ```
# Link de Referencia 
``` https://pypi.org/project/Flask-SocketIO/ ```
``` https://flask-socketio.readthedocs.io/en/latest/index.html```
``` https://pypi.org/project/Pillow/  ```

``` backgroun-color:cadetblue ```