Manual de Instalación y Configuración del Proyecto de Gestión y Monitoreo de IPs 


*Consideraciones Iniciales 

Antes de comenzar, asegúrese de tener instalados los siguientes programas en su equipo. 
Si no los tiene, descárguelos desde los enlaces indicados: 

-Visual Studio Community 2022: https://visualstudio.microsoft.com/es/vs/community/
-MySQL: https://dev.mysql.com/downloads/installer/  
-Python 3.13:  https://www.python.org/downloads/ 
-Git 2.47.1: https://git-scm.com/downloads/win


*Clonación del Repositorio 

-Abra un terminal y navegue al directorio donde desea clonar el proyecto. 
-Ejecute el siguiente comando:
	git clone https://github.com/xavissj/Desafio-Adaptive-Security.git 
-Entre al directorio del proyecto:       
	cd  Desafio-Adaptive-Security 


*Creación y Activación de un Entorno Virtual 

-Cree el entorno virtual:
	 python -m venv envirtual 


*Active el entorno virtual:  
	-Windows: source envirtual/Scripts/activate 
  	-Linux/Mac: source envirtual/bin/activate 
-Verifique que el entorno esté activado observando el prefijo (envirtual) en el terminal.              
 

*Instalación de Dependencias 
-Asegúrese de estar en el directorio del proyecto y active el entorno virtual si no lo está. 
-Ubicarse en la ruta del /envirtual e instale las dependencias listadas en requirements.txt:  
	pip install -r requirements.txt 

             
*Configuración del Archivo .env 
Ubique el archivo .env en la raíz del proyecto. Si no está visible,
asegúrese de que los archivos ocultos estén habilitados. 
-Edite el archivo .env con las credenciales necesarias; Es importante mencionar que las credenciales ingresadas en el .env de la base de datos
deben coincidir con las configuraciones locales.
	DB_HOST=localhost 
	DB_USER=tu_usuario 
	DB_PASSWORD=tu_contraseña 
	ABUSEIPDB_API_KEY=217b7c0cddc94bc3a0a989dc5d601d611b58ddda59437d3ef87e9506a556017f06a5cfd0c61d838f  
	IPSTACK_API_KEY=1dca04e39bb2c06071d64a01ce2a0192 


-Guarde los cambios. 


*Creación de la Base de Datos 
-Abra el archivo create_db_table.sql ubicado en la raíz del proyecto. 
-Ejecute las queries en su gestor de base de datos MySQL para crear la base de datos y las tablas necesarias. 

*Para insertar datos de ejemplo, abra el archivo datos_para_bd.sql y ejecute las queries proporcionadas. 


*Ejecución del Proyecto 
-Asegúrese de estar en la raíz del proyecto. 
-Ejecute el archivo principal con el siguiente comando: python app.py 

         
-Abra un navegador web e ingrese la siguiente URL:
 	http://127.0.0.1:5000/ 
-Disfrute del proyecto.
  

 
  

 

 
