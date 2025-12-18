import requests
from auxiliares import url_comments,url_users

def get_comments_api():
    try:
        respuesta = requests.get(url_comments)
        if respuesta.status_code == 200:
            print("Solicitud correcta, procesando data...")
            return respuesta.json()
        elif respuesta.status_code == 204:
            print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
        else:
            print(
                f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def get_users_api():
    try:
        respuesta = requests.get(url_users)
        if respuesta.status_code == 200:
            print("Solicitud correcta, procesando data Users...")
            return respuesta.json()
        elif respuesta.status_code == 204:
            print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
        else:
            print(
                f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def post_user_api(json_user):
    try:
        respuesta = requests.post(url_users, json=json_user, timeout=10)
        if respuesta.status_code == 201:
            print("Solicitud correcta, User creado...")
            print(respuesta.text)
        else:
            print(
                f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def put_user_api(id_user, json_user):
    try:
        url = f'{url_users}/{id_user}'
        respuesta = requests.put(url, json=json_user, timeout=10)
        if respuesta.status_code == 200:
            print("Solicitud correcta, User modificado...")
            print(respuesta.text)
        else:
            print(
                f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def delete_user_api(id_user):
    try:
        url = f'{url_users}/{id_user}'
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print("Solicitud correcta, User eliminado...")
        else:
            print(
                f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None