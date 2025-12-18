from datos.conexion import get_session

def insertar_objeto(objeto):
    sesion = get_session()
    try:
        sesion.add(objeto)
        sesion.commit()
        sesion.refresh(objeto)
        print("El objeto se ha guardado correctamente.")
        return objeto.id
    except Exception as error:
        sesion.rollback()
        print(f"Error al guardar el objeto: {error}")
        return None
    finally:
        sesion.close()