from flask import render_template, request, redirect, url_for
import pymysql
import os
import requests
from app import app
from datetime import datetime

# Conexión a la base de datos
def get_db_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except pymysql.MySQLError as e:
        return None

# Función para consultar la API 
def consultar_ipstack(ip):
    print(f"Consultando IPStack para la IP: {ip}")  # Depuración
    api_key = os.getenv("IPSTACK_API_KEY")
    url = f"http://api.ipstack.com/{ip}"
    params = {
        "access_key": api_key
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "ip": data.get("ip"),
                "pais": data.get("country_name", "Desconocido"),
                "ciudad": data.get("city", "Desconocido"),
                "latitud": data.get("latitude"),
                "longitud": data.get("longitude"),
                "codigo_pais": data.get("country_code", "N/A"),
                "codigo_region": data.get("region_code", "N/A"),
                "region": data.get("region_name", "Desconocido"),
                

            }
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def consultar_abuseipdb(ip):
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90 
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "ip": data["data"]["ipAddress"],
                "reputation": data["data"]["abuseConfidenceScore"],
                "totalReports": data["data"]["totalReports"],
                "lastReportedAt": data["data"]["lastReportedAt"]
            }
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}    


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/buscar_ip', methods=['GET', 'POST'])
def buscar_ip():
    datos_ipstack = None
    datos_abuseipdb = None
    ip = None
    if request.method == 'POST':
        ip = request.form.get('ip')
        if ip:
            datos_ipstack = consultar_ipstack(ip)
            datos_abuseipdb = consultar_abuseipdb(ip)
    return render_template('buscar_ip.html', datos_ipstack=datos_ipstack, datos_abuseipdb=datos_abuseipdb, ip=ip)



@app.route('/dashboard')
def dashboard():
    connection = get_db_connection()
    f_actual = datetime.now()
    act = f_actual.strftime("%d-%m-%Y %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM analisis_ip")
    datos = cursor.fetchall()  
    cursor.execute("SELECT * FROM analisis_ip ORDER BY total_reportes DESC  LIMIT 5")
    top = cursor.fetchall() 
    cursor.execute(""" SELECT a.*, sub.cantidad FROM analisis_ip a
                        JOIN ( SELECT pais, COUNT(*) AS cantidad
                        FROM analisis_ip
                        GROUP BY pais) sub ON a.pais = sub.pais ORDER BY sub.cantidad DESC LIMIT 5;""")
    paises = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('dashboard.html', datos=datos, act=act, top=top, paises=paises)


@app.route('/gestionar_ip')
def gestionar_ip():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM analisis_ip")
    datos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('gestionar_ip.html', datos=datos)


@app.route('/editar_ip', methods=['GET', 'POST'])
def editar_ip():
    connection = get_db_connection()
    id_edit = request.args.get('id')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM analisis_ip where id="+id_edit)
    datos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('editar_ip.html', datos=datos)

@app.route('/eliminar_ip', methods=['GET'])
def eliminar_ip(): 
    connection = get_db_connection() 
    id_delete = request.args.get('id')
    cursor = connection.cursor() 
    cursor.execute("DELETE FROM analisis_ip WHERE id=%s", (id_delete,)) 
    connection.commit() 
    cursor.close() 
    connection.close() 
    return redirect(url_for('gestionar_ip'))

def calcular_estado(reputation):
    try:
        reputation = int(reputation)
        if 0 <= reputation <= 25:
            return "Confiable"
        elif 11 <= reputation <= 50:
            return "Sospechosa"
        elif 51 <= reputation <= 100:
            return "Maliciosa"
        else:
            return "Sin Datos"
    except ValueError:
        return "Puntaje inválido"

@app.route('/agregar_bd', methods=['POST'])
def agregar_bd():
     if request.method == 'POST':        
        direccion_ip = request.form.get('direccion_ip')
        pais = request.form.get('pais') 
        ciudad = request.form.get('ciudad')
        try:
            indice_reputacion = request.form.get('indice_reputacion') 
            print(f"Consultando indice reputacion: {indice_reputacion}")
        except:
            indice_reputacion= 0
        estado = calcular_estado(indice_reputacion)
        latitud = request.form.get('latitud') 
        longitud = request.form.get('longitud') 
        total_reportes = request.form.get('total_reportes')
        ultimo_reporte = request.form.get('ultimo_reporte') 
        if not ultimo_reporte:  
            ultimo_reporte = "Sin Datos"        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO analisis_ip (direccion_ip, pais, ciudad, indice_reputacion, estado, latitud, longitud, total_reportes, ultimo_reporte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(direccion_ip, pais, ciudad, indice_reputacion, estado, latitud, longitud, total_reportes, ultimo_reporte))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('buscar_ip'))

@app.route('/edicion_ip', methods=['POST'])
def edicion_ip():
    if request.method == 'POST':
        id =  request.form.get('id')
        direccion_ip = request.form.get('direccionIP')
        pais = request.form.get('pais') 
        ciudad = request.form.get('ciudad')
        indice_reputacion = request.form.get('indiceReputacion') 
        estado = request.form.get('estado')
        latitud = request.form.get('latitud') 
        longitud = request.form.get('longitud') 
        total_reportes = request.form.get('totalReportes')
        ultimo_reporte = request.form.get('ultimoReporte') 
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE analisis_ip SET pais = %s, ciudad = %s, indice_reputacion = %s, estado = %s, 
                            latitud = %s, longitud = %s, total_reportes = %s, ultimo_reporte = %s WHERE id = %s """,
                            (pais, ciudad, indice_reputacion, estado, latitud, longitud, total_reportes, ultimo_reporte,id))
        connection.commit() 
        cursor.close()
        connection.close()
    return  redirect(url_for('gestionar_ip'))