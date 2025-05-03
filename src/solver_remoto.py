import json
from cliente import query

def resolver_n_reinas(n: int) -> list[list[int]]:
    """
    Envía n al servidor Haskell y devuelve la lista de soluciones
    parseada de JSON. Si hay error de red o parseo, lanza RuntimeError.
    """
    try:
        raw = query(str(n))
    except ConnectionRefusedError:
        raise RuntimeError("No puedo conectar con el servidor Haskell en 127.0.0.1:3000")
    except Exception as e:
        raise RuntimeError(f"Error de red: {e}")

    try:
        soluciones = json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Respuesta inválida del servidor: {e}\nRaw: {raw!r}")
    return soluciones
