from etl import ProcesoETL

def principal():
    etl = ProcesoETL()
    
    # Definir consulta para el ETL
    consulta = "SELECT * FROM film"
    nombre_tabla = "film_organizado"
    
    # Ejecutar el proceso ETL
    etl.ejecutar_etl(consulta, nombre_tabla)

if __name__ == "__main__":
    principal()
