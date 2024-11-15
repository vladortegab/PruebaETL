# Proyecto de Gestión de Datos ETL con Python y MySQL

Este proyecto consiste en una aplicación que gestiona y ejecuta procesos ETL (Extract, Transform, Load) usando Python, con soporte para bases de datos MySQL. La aplicación permite realizar una carga de datos desde archivos CSV a una base de datos MySQL, así como crear y gestionar tablas necesarias para almacenar dichos datos.

## Requisitos

- Python 3.x
- MySQL Server
- Paquetes de Python: `mysql-connector`, `pandas`, `sqlalchemy`
- Archivos CSV con los datos de entrada
- Archivos SQL para la creación de tablas

## Estructura del Proyecto

.
├── README.md
├── coneccionSpark.py
├── configuracion.py
├── etl.py
├── main.py
├── film.sql
├── rental.csv
├── customer.csv
├── film.csv
├── inventory.csv
└── main.py



## Requisitos Previos

- Python: Asegúrate de tener Python 3.x instalado. Puedes verificarlo ejecutando python --version.

- MySQL: Instala MySQL en tu sistema y asegúrate de configurar un usuario y contraseña válidos.

- Librerías Python: Instala las librerías requeridas ejecutando el siguiente comando:

Para instalar las librerías necesarias, ejecuta el siguiente comando:

    ```bash
    pip install pandas sqlalchemy pymysql mysql-connector-python
   
    ```

## Configuración 
# 1. Clonar el Repositorio
Clona el repositorio en tu máquina:

    ```bash
    git clone https://github.com/vladortegab/PruebaETL
    cd Prueba Tecnica
   
    ```
    

# 2. Configurar MySQL
Crea un usuario en MySQL (o usa un usuario existente) y otórgale permisos suficientes para crear bases de datos y tablas.

Actualiza las credenciales de conexión en el archivo de configuración de la aplicación o directamente en el código en la clase 
_Config_

    ```bash
    class Config:
    DB_HOST = "localhost"
        DB_USER = "root"
        DB_PASSWORD = "tu_password*"
        DB_NAME = "films"
        CSV_FILES = ['customer.csv', 'film.csv', 'inventory.csv', 'rental.csv', 'store.csv']
   
    ```


# 3. Ejecutar el Script de Creación de Base de Datos
Ejecuta el script SQL para crear las tablas:


    ```bash
    mysql -u root -p < scripts/filmase.sql
    Nota: Cambia root y password según sea necesario.
   
    ```





## Uso de la Aplicación
La aplicación permite gestionar y realizar consultas de negocio sobre los datos de la base de datos peliculas. A continuación, algunos ejemplos de uso:

Crear base de datos y tablas: Se ejecuta al iniciar el script main.py, si las tablas no existen.
Cargar datos de CSV a MySQL: Los datos se cargan automáticamente desde los archivos CSV especificados en el directorio data/.
Consultas de Negocio: Puedes realizar análisis exploratorios y consultas personalizadas directamente en la base de datos MySQL.