import os
import subprocess

def restaurar_bd():
    usuario = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    db_name = os.getenv("DB_NAME", "nombre_base_de_datos")
    sql_file = "db/respaldo.sql"

    try:
        # Crear la base de datos
        subprocess.run(
            f"mysql -u {usuario} -p{password} -e 'CREATE DATABASE IF NOT EXISTS {db_name};'",
            shell=True,
            check=True,
        )
        # Importar los datos
        subprocess.run(
            f"mysql -u {usuario} -p{password} {db_name} < {sql_file}",
            shell=True,
            check=True,
        )
        print("Base de datos restaurada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al restaurar la base de datos: {e}")

if __name__ == "__main__":
    restaurar_bd()
