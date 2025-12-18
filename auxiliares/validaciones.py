import re

def validar_correo(email: str) -> bool:
    regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}$"
    return re.fullmatch(regex, str(email)) is not None