class Configuracion:
    # Configuración de Spark
    JAR_SPARK = "C:\Spark\spark-3.5.3-bin-hadoop3\jars\mysql-connector-j-9.1.0"
    NOMBRE_APP_SPARK = "AplicacionETL"
    
    # Configuración de conexión a MySQL
    URL_JDBC = "jdbc:mysql://localhost:3307/filmdb"
    PROPIEDADES_MYSQL = {
        "user": "root",
        "password": "admin",
        "driver": "com.mysql.cj.jdbc.Driver"
    }
