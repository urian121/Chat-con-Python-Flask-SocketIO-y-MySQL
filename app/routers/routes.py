from flask import render_template, session, request


def viewCrearCuentaUsuario():
    if request.method == 'GET':
        if 'conectado' in session:
            return render_template('public/home.html')
        else:
            return render_template('public/login/crearCuenta.html')
    else:
        return render_template('public/home.html')
    
    
   
    
def linkrecuperarMiCuentaUsuario():
    if 'conectado' in session:
        return render_template('public/home.html')
    else:
        return render_template('public/login/recuperarClave.html')
   
    
    