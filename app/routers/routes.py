from flask import render_template, session


def linkCrearCuentaUsuario():
    if 'conectado' in session:
        return render_template('public/index.html')
    else:
        return render_template('public/login/crearCuenta.html')
   
    
def linkrecuperarMiCuentaUsuari():
    if 'conectado' in session:
        return render_template('public/index.html')
    else:
        return render_template('public/login/recuperarClave.html')