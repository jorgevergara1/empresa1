from app import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
from mysql.connector.errors import Error


# Importando conexión a BD 
from controllers.funciones_empleado import *

PATH_URL = "empleados" #carpeta templates/empleados


@app.route('/registrar-empleado', methods=['GET'])
def ViewFormEmpleados():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/form-empleado.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    

@app.route('/form-registrar-empleado', methods=['POST'])
def formEmpleado():
    if 'conectado' is session:
        if 'foto_perfil' in request.files:
            foto_perfil = request.files['foto_perfil']
            resultado = procesar_form_empleado(request.form, foto_perfil)
            if resultado:
                return redirect(url_for('lista_empleados'))
            else:
                flash('El empleado NO fue registrado.', 'error')
                return render_template(f'{PATH_URL}/form_empleado.html')
        else:
            flash('primero debes iniciar sesión.', 'error')
            return redirect(url_for('inicio'))
        

@app.route('/lista-de-empleados', methods=['GET'])
def lista_empleados():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/lista_empleados.html', empleados=sql_lista_empleadosBD())
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    

@app.route("/detalles-empleado/", methods=['GET'])
@app.route("/detalles-empleado/<int:idEmpleado>", methods=['GET'])
def detalleEmpleado(idEmpleado=None):
    if 'conectado' in session:
    # Verificamos si el parámetro idEmpleado es None o no está presente en la URl
        if idEmpleado is None:
            return redirect(url_for('inicio'))
        else:
            detalle_empleado = sql_detalles_empleadoBD(idEmpleado) or []
            return render_template(f'{PATH_URL}/detalles_empleado.html', detalle_empleado=detalle_empleado)
    else: 
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    

# Buscado de Empleados
@app.route("/buscando-empleado", methods= ['POST']) 
def ViewBuscarEmpleadoBD():
    resultadoBusqueda = buscarEmpleadoBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URL}/resultado_busqueda_empleado.html')
    else:
        return jsonify({'fin': 0})


@app.route("/editar-empleados/<int:id", methods=['GET'])
def viewEditarempleado(id):
    if 'conectado' in session:
        respuestaEmpleado = buscarEmpleadoUnico(id)
        if respuestaEmpleado:
            return render_template(f'{PATH_URL}/form_empleado_update.html', respuestaEmpleado=respuestaEmpleado)
        else:
            flash('El empleado no existe', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))
    

# Recibir formulario para actualizar información de empleado
@app.route('/actualizar-empleado', methods=['POST'])
def actualizarEmpleado():
    resultData = procesar_Actualizacion_form(request)
    if resultData:
        return redirect(url_for('lista_empleados'))
    

@app.route("/lista-de-usuarios", methods=['GET'])
def usuarios():
    if 'conectado' in session:
        resp_usuariosBD = lista_usuariosBD()
        return render_template('usuarios/lista_usuarios.html', resp_usuariosBD=resp_usuariosBD)
    else: 
        return redirect(url_for('inicioCpanel'))
    

@app.route('/borrar-usuario/<string:id>', methods=['GET'])
def borrarUsuario(id):
    resp= eliminarUsuario(id)
    if resp:
        flash('El usuario fue eliminado correctamente', 'success')
        return redirect(url_for('usuarios'))
    

@app.route('/borrar-empleado/<string:id_empleado>/<string.foto_perfil>', methods=['GET'])
def borrarEmpleado(id_empleado, foto_perfil):
    resp = eliminarEmpleado(id_empleado, foto_perfil)
    if resp:
        flash('el empleado fue eliminado correctamente', 'success')
        return redirect(url_for('lista_empleados'))
    

@app.route("/descargar-informe-empleados/", methods=['GET'])
def reporteBD():
    if 'conectado' in session:
        return generarReportesExcel)
    else:
        flash(' Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))