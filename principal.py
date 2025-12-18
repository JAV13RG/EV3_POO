from negocio.negocio_usuario import registrar_usuario, iniciar_sesion
from interfaces_usuario import menu_inicial
# obtener_data_usuarios_api(url_usuarios)
# listado_usuarios_db()
# crear_user_api(url_usuarios)
# eliminar_user_api(url_usuarios)
# obtener_data_publicaciones(url_publicaciones)
# listado_publicaciones()
# registrar_usuario()

def app():
    while True:
        opcion = menu_inicial()

        if opcion == 1:
            registrar_usuario()

        elif opcion == 2:
            ok = iniciar_sesion()
            if ok:
                print("Iniciando sistema...")

        elif opcion == 3:
            print("Sección pruebas (API/CRUD) ...")

        elif opcion == 0:
            print("Saliendo...")
            break

if __name__ == "__main__":
    app()