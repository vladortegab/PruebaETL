from pyspark.sql import SparkSession
import os
from sqlalchemy import create_engine


class ETLProcess:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.spark = SparkSession.builder \
            .appName("FilmsETL") \
            .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.26") \
            .getOrCreate()

    def extract_data(self):
        dataframes = []
        for csv_file in self.config.CSV_FILES:
            file_path = os.path.join(os.path.dirname(__file__), csv_file)
            df = self.spark.read.option("header", "true").csv(file_path)
            dataframes.append(df)
            self.logger.info(f"Datos extraídos desde {csv_file}")
        return dataframes

    def transform_data(self, dataframes):
        self.logger.info("Iniciando transformación de datos")
        return dataframes  

    def load_data(self, dataframes):
        engine = create_engine(f'mysql+pymysql://{self.config.DB_USER}:{self.config.DB_PASSWORD}@{self.config.DB_HOST}/{self.config.DB_NAME}')
        table_names = ['customer', 'film', 'inventory', 'rental', 'store']
        for df, table in zip(dataframes, table_names):
            pandas_df = df.toPandas() 
            pandas_df.to_sql(name=table, con=engine, if_exists='append', index=False)
            self.logger.info(f"Datos cargados en la tabla '{table}'")

    def run_etl(self):
        dataframes = self.extract_data()
        transformed_data = self.transform_data(dataframes)
        self.load_data(transformed_data)