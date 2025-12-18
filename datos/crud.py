from datos.conexion import get_session

def obtener_por_id(modelo, id_objeto: int):
    sesion = get_session()
    try:
        return sesion.query(modelo).get(id_objeto)
    finally:
        sesion.close()

def actualizar_por_id(modelo, id_objeto: int, cambios: dict) -> bool:
    sesion = get_session()
    try:
        obj = sesion.query(modelo).get(id_objeto)
        if not obj:
            print("No existe en BD local.")
            return False

        for k, v in cambios.items():
            if hasattr(obj, k):
                setattr(obj, k, v)

        sesion.commit()
        print("Actualizado en BD local.")
        return True
    except Exception as e:
        sesion.rollback()
        print(f"Error al actualizar en BD local: {e}")
        return False
    finally:
        sesion.close()

def eliminar_por_id(modelo, id_objeto: int) -> bool:
    sesion = get_session()
    try:
        obj = sesion.query(modelo).get(id_objeto)
        if not obj:
            print("No existe en BD local.")
            return False
        sesion.delete(obj)
        sesion.commit()
        print("Eliminado en BD local.")
        return True
    except Exception as e:
        sesion.rollback()
        print(f"Error al eliminar en BD local: {e}")
        return False
    finally:
        sesion.close()