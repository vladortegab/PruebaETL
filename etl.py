from coneccionSpark import ConectorSpark
from monitoreo import Monitoreo

class ProcesoETL:
    def __init__(self):
        self.conector_spark = ConectorSpark()
        self.monitoreo = Monitoreo()

    def extraer(self, consulta):
        """Extraer datos desde MySQL usando Spark"""
        self.monitoreo.registrar(f"Ejecutando consulta: {consulta}")
        df = self.conector_spark.leer_datos(consulta)
        self.monitoreo.registrar(f"Datos extraídos: {df.count()} registros")
        return df

    def transformar(self, df):
        """Transformación de datos"""
        self.monitoreo.registrar("Transformando datos")
        return df

    def cargar(self, df, nombre_tabla):
        """Cargar datos transformados en otra tabla"""
        self.monitoreo.registrar(f"Cargando datos en la tabla {nombre_tabla}")
        df.write.jdbc(url="jdbc:mysql://localhost:3307/filmdb", table=nombre_tabla, mode="overwrite", properties={"user": "root", "password": "admin", "driver": "com.mysql.cj.jdbc.Driver"})
    
    def ejecutar_etl(self, consulta, nombre_tabla):
        """Ejecutar el proceso completo de ETL"""
        self.monitoreo.registrar("Iniciando proceso ETL")
        df = self.extraer(consulta)
        df = self.transformar(df)
        self.cargar(df, nombre_tabla)
        self.monitoreo.registrar("Proceso ETL finalizado")
