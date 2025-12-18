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
