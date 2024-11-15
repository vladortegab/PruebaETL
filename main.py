from configuracion import Config
from configuracion import LoggerSetup 
from coneccionSpark import DatabaseConnector 
from etl import ETLProcess 

# Clase principal de la aplicación ETL
class FilmsETLApp:
    def __init__(self):
        self.config = Config()
        self.logger = LoggerSetup().get_logger()
        self.db_connector = DatabaseConnector(self.config)
        self.etl_process = ETLProcess(self.config, self.logger)

    def run(self):
        self.logger.info("Iniciando proceso ETL del Proyecto Films")
        self.db_connector.create_database_if_not_exists(self.logger)
        self.etl_process.run_etl()
        self.logger.info("Proceso ETL completado")

if __name__ == '__main__':
    app = FilmsETLApp()
    app.run()