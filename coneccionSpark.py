from pyspark.sql import SparkSession
from configuracion import Configuracion

class ConectorSpark:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName(Configuracion.NOMBRE_APP_SPARK) \
            .config("spark.jars", Configuracion.JAR_SPARK) \
            .getOrCreate()
    
    def leer_datos(self, consulta):
        """Leer datos desde MySQL usando Spark"""
        return self.spark.read.jdbc(url=Configuracion.URL_JDBC, table=f"({consulta}) as consulta_films", properties=Configuracion.PROPIEDADES_MYSQL)
    
    def detener(self):
        """Detener la sesión Spark"""
        self.spark.stop()

