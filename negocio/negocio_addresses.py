from modelos import Address
from datos import insertar_objeto


def crear_direccion(calle, departamento, ciudad, codigo_postal, geolocalizacion_id):
    direccion = Address(
        street=calle,
        suite=departamento,
        city=ciudad,
        zipcode=codigo_postal,
        geoId=geolocalizacion_id
    )
    try:
        return insertar_objeto(direccion)
    except Exception as error:
        print(f'Error al guardar la dirección: {error}')
        return None
