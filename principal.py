from negocio.negocio_usuario import registrar_usuario, iniciar_sesion
from interfaces_usuario import menu_inicial
from interfaces_usuario.menus_app import menu_pruebas


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