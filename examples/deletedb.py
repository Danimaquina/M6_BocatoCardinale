import mongoengine as me

# Configura la conexión a la base de datos
def borrar_base_de_datos(nombre_db):
    # Conecta a la base de datos
    me.connect(nombre_db, host="mongodb://localhost:27017/" + nombre_db)
    
    # Borra la base de datos completa
    me.connection.get_db().client.drop_database(nombre_db)
    print(f"La base de datos '{nombre_db}' ha sido borrada completamente.")

if __name__ == "__main__":
    # Nombre de la base de datos que quieres borrar
    nombre_db = "boccato_di_cardinale"  # Cambia esto por el nombre de tu base de datos
    
    # Llama a la función para borrar la base de datos
    borrar_base_de_datos(nombre_db)