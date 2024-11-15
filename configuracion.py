import logging
import sys
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from pyspark.sql import SparkSession
import os


# Clase de configuración
class Config:
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "Admin123*"
    DB_NAME = "films"
    CSV_FILES = ['customer.csv', 'film.csv', 'inventory.csv', 'rental.csv', 'store.csv']

# Clase de configuración de logging
class LoggerSetup:
    def __init__(self):
        self.logger = logging.getLogger('FILM_ETL')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
    def get_logger(self):
        return self.logger