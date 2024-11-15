import mysql


class DatabaseConnector:
    def __init__(self, config):
        self.config = config

    def create_mysql_connection(self, database=None):
        return mysql.connector.connect(
            host=self.config.DB_HOST,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD,
            database=database
        )

    def create_database_if_not_exists(self, logger):
        try:
            conn = self.create_mysql_connection()
            cursor = conn.cursor()
            cursor.execute(f"SHOW DATABASES LIKE '{self.config.DB_NAME}';")
            if not cursor.fetchone():
                cursor.execute(f"CREATE DATABASE {self.config.DB_NAME}")
                conn.commit()
                logger.info(f"Base de datos '{self.config.DB_NAME}' creada.")
            else:
                logger.info(f"La base de datos '{self.config.DB_NAME}' ya existe.")
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            logger.error(f"Error al crear la base de datos: {e}")