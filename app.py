from flask import Flask,  render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)
app = Flask(__name__, static_folder='static')


# Configuraciones globales (puedes añadir más si es necesario)
app.config['DB_HOST'] = os.getenv("DB_HOST")
app.config['DB_USER'] = os.getenv("DB_USER")
app.config['DB_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['DB_NAME'] = os.getenv("DB_NAME")
app.config['ABUSEIPDB_API_KEY'] = os.getenv("ABUSEIPDB_API_KEY")
app.config['IPSTACK_API_KEY'] = os.getenv("IPSTACK_API_KEY")

# Importar las rutas desde main.py
from main import *

# Ejecutar la aplicación si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True)





