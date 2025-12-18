from datos.conexion import get_session
from modelos import Company, User, Usuario

def obtener_listado_objetos(modelo):
    sesion = get_session()
    try:
        return sesion.query(modelo).all()
    finally:
        sesion.close()

def obtener_user_name(valor):
    sesion = get_session()
    try:
        return sesion.query(User).filter(User.name.like(f"%{valor}%")).first()
    finally:
        sesion.close()

def obtener_usuario_nombre(valor):
    sesion = get_session()
    try:
        return sesion.query(Usuario).filter(Usuario.usuario.like(f"%{valor}%")).first()
    finally:
        sesion.close()

def obtener_company_name(valor):
    sesion = get_session()
    try:
        return sesion.query(Company).filter(Company.name.like(f"%{valor}%")).first()
    finally:
        sesion.close()