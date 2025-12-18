from negocio.negocio_usuario import registrar_usuario, iniciar_sesion
from interfaces_usuario import menu_inicial
from negocio.negocio_users import (
    obtener_users_api,
    crear_user_api,
    modificar_user_api,
    eliminar_user_api,
    listado_usuarios_db
)

def menu_pruebas():
    while True:
        print("\n=== SECCIÓN PRUEBAS API / CRUD ===")
        print("[1] GET usuarios desde API y guardar en DB")
        print("[2] POST usuario (API)")
        print("[3] PUT usuario (API)")
        print("[4] DELETE usuario (API)")
        print("[5] LISTAR usuarios DB")
        print("[0] Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            obtener_users_api()

        elif opcion == "2":
            crear_user_api()

        elif opcion == "3":
            modificar_user_api()

        elif opcion == "4":
            eliminar_user_api()

        elif opcion == "5":
            listado_usuarios_db()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")

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
            menu_pruebas()

        elif opcion == 0:
            print("Saliendo...")
            break

if __name__ == "__main__":
    app()