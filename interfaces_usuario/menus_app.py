from negocio.negocio_users import (
    obtener_users_api,
    crear_user_api,
    modificar_user_api,
    eliminar_user_api,
    listado_usuarios_db
)

def menu_inicial() -> int:
    print("\n=== MENÚ PRINCIPAL ===")
    print("[1] Registrar Nuevo Usuario")
    print("[2] Iniciar Sesión")
    print("[3] Sección Pruebas (API/CRUD)")
    print("[0] Salir")

    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion.isdigit():
            opcion_int = int(opcion)
            if opcion_int in (0, 1, 2, 3):
                return opcion_int
        print("❌ Opción inválida. Intente nuevamente.")

def menu_pruebas():
    while True:
        print("\n=== SECCIÓN PRUEBAS API / CRUD ===")
        print("[1] GET usuarios desde API y guardar en DB")
        print("[2] POST usuario")
        print("[3] PUT usuario")
        print("[4] DELETE usuario")
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