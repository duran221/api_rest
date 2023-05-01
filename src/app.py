#Import Flask library:
from flask import Flask,jsonify,request
import json

#Import dictionary config.
from config import config
#Import connector for Postgre SQL.
import psycopg2

#import Models
from models.estudiante import  Estudiante
from models.docente import  Docente
from models.usuario import  Usuario
from models.asignatura import Asignatura
##conection db
from conexion_db import *

#Inicialite app:
app = Flask(__name__)

"""*****************************************************************************************************************************"""

@app.route('/estudiantes',methods=['GET'])
def get_estudiantes():
    estudiantes = []
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute('''SELECT * FROM estudiantes''')
        datos = cur.fetchall()
        for fila in datos:
            estudiante = Estudiante(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
            jsonEstudiante= {'documento':estudiante.documento,'nombres':estudiante.nombres,'apellidos':estudiante.apellidos,'fecha_nacimiento':estudiante.fecha_nacimiento,'edad':estudiante.edad,'genero':estudiante.genero,'direccion':estudiante.direccion,'promedio':estudiante.promedio}
            estudiantes.append(jsonEstudiante)
        cur.close()

        return jsonify({'estudiantes':estudiantes,'mensaje':"Estudiantes listados."})

    except Exception as ex:
        return f"Error {ex}"


@app.route('/estudiantes/<codigo>',methods=['GET'])
def get_estudiante(codigo):
    try:
        estudiante= obtener_estudiante_db(codigo)
        if estudiante != None:
            jsonEstudiante= {'documento':estudiante.documento,'nombres':estudiante.nombres,'apellidos':estudiante.apellidos,'fecha_nacimiento':estudiante.fecha_nacimiento,'edad':estudiante.edad,'genero':estudiante.genero,'direccion':estudiante.direccion,'promedio':estudiante.promedio}
            asignaturas_estudiante= obtener_asignaturas_estudiante_db(codigo)
            if(len(asignaturas_estudiante)>0):
                json_asignaturas = []
                for asignatura in asignaturas_estudiante:
                    json_asignatura = {'codigo_asignatura': asignatura.codigo_asignatura,
                                   'docente_encargado': asignatura.codigo_docente,
                                   'nombre_asignatura': asignatura.nombre_asignatura,
                                   'numero_creditos': asignatura.numero_creditos,
                                   'nota_asignatura':asignatura.nota_asignatura}
                    json_asignaturas.append(json_asignatura)
                jsonEstudiante['asignaturas'] = json_asignaturas

            return jsonify({'estudiante':jsonEstudiante,'mensaje':"Estudiante listado."})

        else:
            return jsonify({'mensaje':"Estudiante no encontrado."}),404
        cur.close()
    except Exception as ex:
        return f"Error {ex}"


@app.route('/estudiantes',methods=['POST'])
def registrar_estudiante():
    try:
        conn, cur = crear_conexion()
        estudiante = (request.json['documento'],request.json['nombres'],request.json['apellidos'],
                                request.json['fecha_nacimiento'],request.json['edad'],request.json['genero'],
                                request.json['direccion'],request.json['promedio'])
        # Select all products from the table
        sql=f'''INSERT INTO estudiantes (documento,nombres,apellidos,fecha_nacimiento,edad,genero,direccion,promedio)
                    VALUES ('{estudiante.documento}','{estudiante.nombres}','{estudiante.apellidos}','{estudiante.fecha_nacimiento}',
                    {estudiante.edad},'{estudiante.genero}','{estudiante.direccion}',{estudiante.promedio})'''
        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje':"Estudiante registrado"})
        cur.close()
    except Exception as ex:
        return f"Error Registrando el curso {ex}"


@app.route('/estudiantes/<codigo>',methods=['DELETE'])
def eliminar_estudiante(codigo):
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute(f'''DELETE FROM estudiantes WHERE documento = {codigo}''')
        conn.commit()
        cur.close()
        return jsonify({'mensaje':"Estudiante eliminado."})

    except Exception as ex:
        return f"Error {ex}"

@app.route('/estudiantes/<codigo>', methods=['PUT'])
def actualizar_estudiante(codigo):
    try:
        conn, cur = crear_conexion()
        estudiante = Estudiante(request.json['documento'], request.json['nombres'], request.json['apellidos'],
                                request.json['fecha_nacimiento'], request.json['edad'], request.json['genero'],
                                request.json['direccion'], request.json['promedio'])
        # Select all products from the table
        sql = f'''UPDATE estudiantes SET
                     documento='{estudiante.documento}',nombres='{estudiante.nombres}',apellidos= '{estudiante.apellidos}',fecha_nacimiento='{estudiante.fecha_nacimiento}',
                    edad={estudiante.edad},genero= '{estudiante.genero}',direccion='{estudiante.direccion}',promedio= {estudiante.promedio}
                    WHERE documento = '{estudiante.documento}' '''

        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje': "Estudiante actualizado"})
        cur.close()
    except Exception as ex:
        return f"Error Actualizando el curso {ex}"

"""*****************************************************************************************************************************"""


@app.route('/docentes',methods=['GET'])
def get_docentes():
    docentes = []
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute('''SELECT * FROM docentes''')
        datos = cur.fetchall()
        for fila in datos:
            docente = Docente(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
            json_docente= {'codigo_docente':docente.codigo_docente,'documento':docente.documento,'nombres':docente.nombres,'apellidos':docente.apellidos,'fecha_nacimiento':docente.fecha_nacimiento,'edad':docente.edad,'genero':docente.genero,'direccion':docente.direccion,'salario':docente.salario}
            docentes.append(json_docente)
        cur.close()
        return jsonify({'docentes':docentes,'mensaje':"Docentes listados."})

    except Exception as ex:
        return f"Error {ex}"

def obtener_docente_db(codigo):
    conn, cur = crear_conexion()
    # Select all products from the table
    cur.execute(f'''SELECT * FROM docentes WHERE codigo_docente = {codigo}''')
    fila = cur.fetchone()
    if fila != None:
        docente = Docente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
        return docente
    else:
        return None

def obtener_estudiante_db(codigo):
    conn, cur = crear_conexion()
    # Select all products from the table
    cur.execute(f'''SELECT * FROM estudiantes WHERE documento = '{codigo}' ''')
    fila = cur.fetchone()
    if fila != None:
        estudiante = Estudiante(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
        return estudiante
    else:
        return None

def obtener_asignatura_db(codigo):
    conn, cur = crear_conexion()
    # Select all products from the table
    cur.execute(f'''SELECT * FROM asignaturas WHERE codigo_asignatura = {codigo}''')
    fila = cur.fetchone()
    if fila != None:
        asignatura = Asignatura(fila[0], fila[1], fila[2], fila[3])
        return asignatura
    else:
        return None

def obtener_asignaturas_estudiante_db(documento):
    conn, cur = crear_conexion()
    asignaturas = []
    # Select all products from the table
    cur.execute(f'''SELECT * FROM estudiantes es join estudiantes_asignaturas est_as on es.documento= est_as.documento_estudiante
                    join asignaturas asig on est_as.codigo_asignatura=asig.codigo_asignatura
                    where es.documento = '{documento}' ''')
    datos = cur.fetchall()
    for fila in datos:
        asignatura = Asignatura(fila[12], fila[13], fila[14], fila[15])
        asignatura.nota_asignatura = fila[11]

        asignaturas.append(asignatura)
    return asignaturas

@app.route('/docentes/<codigo>',methods=['GET'])
def get_docente(codigo):
    try:
        docente=obtener_docente_db(codigo)
        if docente != None:
            json_docente= {'codigo_docente':docente.codigo_docente,'documento':docente.documento,'nombres':docente.nombres,'apellidos':docente.apellidos,'fecha_nacimiento':docente.fecha_nacimiento,'edad':docente.edad,'genero':docente.genero,'direccion':docente.direccion,'salario':docente.salario}
            return jsonify({'docente':json_docente,'mensaje':"Docente listado."})
        else:
            return jsonify({'mensaje':"Docente no encontrado."}),404
        cur.close()

    except Exception as ex:
        return f"Error {ex}"


@app.route('/docentes',methods=['POST'])
def registrar_docente():
    try:
        conn, cur = crear_conexion()
        docente = Docente(request.json['codigo_docente'],request.json['documento'],request.json['nombres'],request.json['apellidos'],
                                request.json['fecha_nacimiento'],request.json['edad'],request.json['genero'],
                                request.json['direccion'],request.json['salario'])
        # Select all products from the table
        sql=f'''INSERT INTO docentes (codigo_docente,documento,nombres,apellidos,fecha_nacimiento,edad,genero,direccion,salario)
                    VALUES ('{docente.codigo_docente}','{docente.documento}','{docente.nombres}','{docente.apellidos}','{docente.fecha_nacimiento}',
                    {docente.edad},'{docente.genero}','{docente.direccion}',{docente.salario})'''
        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje':"Docente registrado"})
        cur.close()
    except Exception as ex:
        return f"Error Registrando el Docente {ex}"


@app.route('/docentes/<codigo>',methods=['DELETE'])
def eliminar_docente(codigo):
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute(f'''DELETE FROM docentes WHERE documento = {codigo}''')
        conn.commit()
        cur.close()
        return jsonify({'mensaje':"Docente eliminado."})
    except Exception as ex:
        return f"Error {ex}"

@app.route('/docentes/<codigo>', methods=['PUT'])
def actualizar_docente(codigo):
    try:
        conn, cur = crear_conexion()
        docente = Docente(request.json['codigo_docente'],request.json['documento'], request.json['nombres'], request.json['apellidos'],
                                request.json['fecha_nacimiento'], request.json['edad'], request.json['genero'],
                                request.json['direccion'], request.json['salario'])
        # Select all products from the table
        sql = f'''UPDATE docentes SET
                     codigo_docente='{docente.codigo_docente}', documento='{docente.documento}',nombres='{docente.nombres}',apellidos= '{docente.apellidos}',fecha_nacimiento='{docente.fecha_nacimiento}',
                    edad={docente.edad},genero= '{docente.genero}',direccion='{docente.direccion}',salario= {docente.salario}
                    WHERE codigo_docente = '{docente.codigo_docente}' '''

        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje': "Docente actualizado"})
        cur.close()
    except Exception as ex:
        return f"Error Actualizando el Docente {ex}"

"""*****************************************************************************************************************************"""


@app.route('/asignaturas',methods=['GET'])
def get_asignaturas():
    asignaturas = []
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute('''SELECT * FROM asignaturas''')
        datos = cur.fetchall()
        for fila in datos:
            asignatura = Asignatura(fila[0],fila[1],fila[2],fila[3])
            json_asignatura= {'codigo_asignatura':asignatura.codigo_asignatura,'docente_encargado':asignatura.codigo_docente,'nombre_asignatura':asignatura.nombre_asignatura,'numero_creditos':asignatura.numero_creditos}

            docente = obtener_docente_db(asignatura.codigo_docente)
            if docente != None:
                json_asignatura['docente_encargado'] = {'codigo_docente': docente.codigo_docente,
                                                        'documento': docente.documento, 'nombres': docente.nombres,
                                                        'apellidos': docente.apellidos,
                                                        'fecha_nacimiento': docente.fecha_nacimiento,
                                                        'edad': docente.edad, 'genero': docente.genero,
                                                        'direccion': docente.direccion, 'salario': docente.salario}
            asignaturas.append(json_asignatura)
        cur.close()
        return jsonify({'asignaturas':asignaturas,'mensaje':"Asignaturas listados."})

    except Exception as ex:
        return f"Error {ex}"


@app.route('/asignaturas/<codigo>',methods=['GET'])
def get_asignatura(codigo):
    try:
        asignatura = obtener_asignatura_db(codigo)
        if asignatura != None:
            json_asignatura = {'codigo_asignatura': asignatura.codigo_asignatura,
                               'docente_encargado': asignatura.codigo_docente,
                               'nombre_asignatura': asignatura.nombre_asignatura,
                               'numero_creditos': asignatura.numero_creditos}

            docente = obtener_docente_db(asignatura.codigo_docente)
            if docente != None:
                json_asignatura['docente_encargado'] = {'codigo_docente': docente.codigo_docente,
                                                        'documento': docente.documento, 'nombres': docente.nombres,
                                                        'apellidos': docente.apellidos,
                                                        'fecha_nacimiento': docente.fecha_nacimiento,
                                                        'edad': docente.edad,
                                                        'genero': docente.genero, 'direccion': docente.direccion,
                                                        'salario': docente.salario}
            return jsonify({'asignatura': json_asignatura, 'mensaje': "Asignatura listada."})
        else:
            return jsonify({'mensaje':"Asignatura no encontrada."}),404
        cur.close()

    except Exception as ex:
        return f"Error {ex}"


@app.route('/asignaturas',methods=['POST'])
def registrar_asignatura():
    try:
        conn, cur = crear_conexion()
        asignatura = Asignatura(request.json['codigo_asignatura'],request.json['codigo_docente'],request.json['nombre_asignatura'],request.json['numero_creditos'])
        # Select all products from the table
        sql=f'''INSERT INTO asignaturas (codigo_asignatura,codigo_docente,nombre_asignatura,numero_creditos)
                    VALUES ('{asignatura.codigo_asignatura}',{asignatura.codigo_docente},'{asignatura.nombre_asignatura}',{asignatura.numero_creditos})'''
        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje':"Asignatura registrada"})
        cur.close()
    except Exception as ex:
        return f"Error Registrando la Asignatura {ex}"

@app.route('/asignaturas/<codigo>',methods=['DELETE'])
def eliminar_asignatura(codigo):
    try:
        conn, cur = crear_conexion()
        # Select all products from the table
        cur.execute(f'''DELETE FROM asignaturas WHERE codigo_asignatura = {codigo}''')
        conn.commit()
        cur.close()
        return jsonify({'mensaje':"Asignatura eliminada."})
    except Exception as ex:
        return f"Error {ex}"

@app.route('/asignaturas/<codigo>', methods=['PUT'])
def actualizar_asignatura(codigo):
    try:
        conn, cur = crear_conexion()
        asignatura = Asignatura(request.json['codigo_asignatura'],request.json['codigo_docente'],request.json['nombre_asignatura'],request.json['numero_creditos'])
        # Select all products from the table
        sql = f'''UPDATE asignaturas SET
                     codigo_asignatura='{asignatura.codigo_asignatura}', codigo_docente={asignatura.codigo_docente},nombre_asignatura='{asignatura.nombre_asignatura}',numero_creditos={asignatura.numero_creditos}
                    WHERE codigo_asignatura = '{asignatura.codigo_asignatura}' '''

        cur.execute(sql)
        conn.commit()
        return jsonify({'mensaje': "Asignatura actualizada"})
        cur.close()
    except Exception as ex:
        return f"Error Actualizando el Docente {ex}"

"""*****************************************************************************************************************************"""

@app.route('/matriculas',methods=['POST'])
def matricular_estudiante():
    try:
        conn, cur = crear_conexion()
        asignatura= obtener_asignatura_db(request.json['codigo_asignatura'])
        estudiante= obtener_estudiante_db(request.json['documento_estudiante'])
        if asignatura!=None and estudiante!=None:
            asignatura.nombre_asignatura = request.json['nota_asignatura']
            # Select all products from the table
            sql=f'''INSERT INTO estudiantes_asignaturas (codigo_asignatura,documento_estudiante,fecha_registro,nota_asignatura)
                        VALUES ('{asignatura.codigo_asignatura}','{estudiante.documento}',current_timestamp,{asignatura.nombre_asignatura})'''
            cur.execute(sql)
            conn.commit()
            return jsonify({'mensaje':"Estudiante matriculado"})
            cur.close()
        else:
            return f"Error el Estudiante o El curso especificado no existen en el sistema"

    except Exception as ex:
        return f"Error Matriculando  el Estudiante en el curso {ex}"
"""*****************************************************************************************************************************"""


def route_not_allowed(error):
    return "<h1>route not found</h1>",404
"""*****************************************************************************************************************************"""

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,route_not_allowed)
    app.run()


    